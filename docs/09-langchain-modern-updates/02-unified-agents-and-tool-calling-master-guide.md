<div dir="rtl">

# الدليل المعماري الشامل: بناء الوكلاء الموحدين واستدعاء الأدوات في LangChain v1+
### Unified Agents (`create_agent`), Docstring Contracts, Graph Topology, and Message Execution Traces (Lecture 59)

---

## 1. الدافع الهندسي: لماذا تفشل النماذج اللغوية المجردة أمام البيانات اللحظية؟

في تطبيقات الذكاء الاصطناعي التوليدي التقليدية (`Plain LLM Apps`)، نُرسل مدخلاً نصياً إلى النموذج (`GPT`, `LLaMA`, `Gemini`) ونستقبل مخرجاً نصياً. لكن هذه النماذج تعاني من قيد فيزيائي صارم يسمى **تاريخ انقطاع التدريب (`Training Cutoff Date`)**.

* النموذج اللغوي لا يمتلك معلومات اليوم؛ فإذا سألته: *"ما هي أخبار الذكاء الاصطناعي اليوم؟"* أو *"ما حالة الطقس في نيويورك الآن؟"*، لن يستطيع الإجابة بدقة لأنه دُرب على بيانات ماضية فقط.
* **الحل المعماري — وكيل الذكاء الاصطناعي (`AI Agent`)**: ربط النموذج اللغوي (الذي يعمل كعقل مفكر) بمجموعة من **الأدوات الخارجية (`Tools / APIs`)**؛ بحيث يقرر النموذج ذاتياً متى يفتقر للمعلومة، ويستدعي الأداة المناسبة لجلب السياق الحي (`Live Context`)، ثم يصيغ الإجابة النهائية.

</div>

```mermaid
flowchart LR
    UserQ["سؤال حي: ما حالة الطقس في نيويورك؟"] --> Brain{"عقل الوكيل (LLM)<br>هل أملك المعلومة في أوزان تدريبي؟"}
    Brain -->|"نعم (معرفة تاريخية)"| DirectAns["إجابة مباشرة للمستخدم"]
    Brain -->|"لا (بيانات لحظية تتجاوز Cutoff Date)"| ToolSelect["تقرير استدعاء الأداة: get_weather(city='New York')"]
    ToolSelect --> ExecTool["تنفيذ الأداة وجلب السياق (Context)"]
    ExecTool -->|"ToolMessage: 'The weather is sunny'"| Synth["صياغة الإجابة النهائية الموثقة"]
    Synth --> FinalOut["إخراج الرد النهائي للمستخدم"]
```

<div dir="rtl">

---

## 2. القفزة المعمارية: من `AgentExecutor` القديم إلى `create_agent` في `LangChain v1+`

في الإصدارات السابقة من LangChain، كان بناء وكيل بسيط يتطلب خطوات يدوية معقدة (إنشاء قالب برومبت `ReAct` يدوياً، ربطه بالنموذج، ثم تغليفه داخل `AgentExecutor`).  
أما في **LangChain v1+**، تم اختزال هذه المعمارية في دالة موحدة واحدة هي **`create_agent`** المستوردة من `langchain.agents`، والتي تُرجع تلقائياً رسماً بيانياً مُجمّعاً من نوع `CompiledStateGraph` فوق محرك **`LangGraph`**.

### أ. تطور طوبولوجيا الرسم البياني (`Graph Topology Evolution`):

</div>

```mermaid
flowchart TD
    subgraph Toolless["1. وكيل بدون أدوات: create_agent(model, tools=[])"]
        direction LR
        S1((START)) --> M1["عقدة النموذج (model)"]
        M1 --> E1((END))
    end

    subgraph WithTools["2. وكيل مزود بأدوات: create_agent(model, tools=[get_weather])"]
        direction LR
        S2((START)) --> M2["عقدة النموذج (model)"]
        M2 -->|"AIMessage: tool_calls"| T2["عقدة الأدوات (tools)"]
        T2 -->|"ToolMessage: Context"| M2
        M2 -->|"إجابة نهائية جاهزة"| E2((END))
    end
```

<div dir="rtl">

* **عندما تكون `tools=[]`**: تكون العقد فقط `['__start__', 'model', '__end__']` — مسار خطي بدون حلقات تكرارية.
* **عند إضافة أداة مثل `get_weather`**: تضاف عقدة `tools` وتتحول المعمارية إلى **رسم بياني دائري (`Cyclic Graph`)** يعود فيه مخرج الأداة إلى النموذج لتوليد الرد النهائي.
* **تنبيه حول المعاملات المهجورة**: معاملات مثل `verbose=True` التي كانت تُمرر لـ `AgentExecutor` القديم لم تعد مدعومة داخل `create_agent` وتطلق خطأ `TypeError`، لأن مراقبة التنفيذ أصبحت تُدار عبر `debug=True` أو تتبع `LangSmith` و `.stream()`.

---

## 3. عقد التوجيه عبر النصوص التوضيحية (`The Docstring Contract`)

السؤال الجوهري: **كيف يعرف النموذج اللغوي أي دالة بايثون يجب أن يستدعيها، وما هي المعاملات المطلوبة؟**

تعتمد آلية `Tool Calling` في LangChain على تحويل دالة بايثون تلقائياً إلى مخطط `JSON Schema` بناءً على 3 ركائز إلزامية:
1. **اسم الدالة (`Function Name`)**: مثل `get_weather`.
2. **توصيف الأنواع (`Type Hints`)**: مثل `city: str -> str` لتعريف نوع البيانات المتوقعة.
3. **النص التوضيحي (`Docstring`)**: النص المكتوب داخل `"""..."""` هو الإشارة الدلالية الأساسية التي يقرأها النموذج ليفهم وظيفة الأداة ومتى يقرّر استدعاءها.

```python
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    return f"The weather in {city} is sunny."
```

> **قاعدة هندسية حاسمة**: كتابة `Docstring` غامض أو ترك دالة بدون `Docstring` قد يؤدي إلى فشل النموذج في استدعاء الأداة أو تمرير معاملات خاطئة تماماً!

---

## 4. عقد الاستدعاء وتفكيك مسار الرسائل (`Agent Invocation & Trace`)

لأن `create_agent` يبني رسماً بيانياً للحالة (`StateGraph`) يعتمد على قائمة الرسائل (`messages`)، فإن تمرير نص خام مباشرة مثل `agent.invoke("What is the weather?")` يُطلق خطأ (`Expected dictionary` / `InvalidUpdateError`).

### الصيغ القياسية المدعومة في الاستدعاء:
1. **الصيغة المهيكلة الكاملة**:
   ```python
   agent.invoke({"messages": [{"role": "user", "content": "What is the weather in New York?"}]})
   ```
2. **الصيغة المختصرة المرنة** (تقبل النص مباشرة داخل مفتاح `messages` وتعامل مع الأخطاء الإملائية بذكاء مثل `"wather"`):
   ```python
   agent.invoke({"messages": "What is the wather in New York?"})
   ```

### تتبع الرسائل الأربعة داخل المخرجات (`response["messages"]`):
عند تشغيل الاستعلام بنجاح، يحتوي سجل المحادثة الناتج على التسلسل الدقيق التالي:
1. **`HumanMessage`**: استعلام المستخدم الأصلي (`What is the weather in New York?`).
2. **`AIMessage` (طلب الأداة)**: استجابة النموذج الفارغة نصياً ولكنها تحتوي على خاصية `tool_calls`:
   ```python
   [{'name': 'get_weather', 'args': {'city': 'New York'}, 'id': 'fc_...', 'type': 'tool_call'}]
   ```
3. **`ToolMessage`**: نتيجة تنفيذ الدالة الفعلية في بايثون (`The weather in New York is sunny.`) مربوطة بنفس الـ `tool_call_id`.
4. **`AIMessage` (الرد النهائي)**: يقوم النموذج بقراءة `ToolMessage` وصياغة الإجابة النهائية الواضحة للمستخدم في `response["messages"][-1].content`.

---

## 5. مصفوفة المفاضلة الهندسية (Legacy AgentExecutor vs LangChain v1 create_agent)

| المعيار الهندسي | النمط القديم (`AgentExecutor + ReAct`) | النمط الحديث (`LangChain v1 create_agent`) |
| :--- | :--- | :--- |
| **المحرك التنفيذي** | حلقة بايثون مغلقة (`Black-box while loop`). | رسم بياني مُجمّع للحالة (`LangGraph CompiledStateGraph`). |
| **التخصيص والتحكم** | صعب جداً؛ يتطلب تجاوز الدوال الداخلية أو Callbacks. | مرن بالكامل عبر طبقات `Middleware` ونقاط التوقف `interrupt_before`. |
| **آلية استدعاء الأدوات** | يعتمد غالباً على تحليل نصوص الـ ReAct (`Thought/Action/Observation`). | يعتمد على `Native Function/Tool Calling` المدمج في النماذج الحديثة بدقة عالية. |
| **المرونة مع المدخلات** | صارم في قوالب النصوص (`PromptTemplate` variables). | موحد عبر حالة `{"messages": [...]}` مع دعم صيغ القاموس أو النصوص أو `HumanMessage`. |
| **الحفظ والبث اللحظي** | دعم محدود للذاكرة متعددة الخطوات. | دعم أصيل للـ `Checkpointers` والبث اللحظي عبر `.stream()`. |

---

## 6. أسئلة المقابلات المتقدمة للـ Senior AI Engineers

### س1: لماذا يُطلق `create_agent` خطأ إذا لم تمرر الأدوات أو مررت `verbose=True`، وما هي البدائل الإنتاجية لمراقبة تنفيذ الوكيل؟
**الإجابة النموذجية:**
دالة `create_agent` في `LangChain v1+` مبنية مباشرة فوق محرك `LangGraph` وليست مجرد غلاف لـ `AgentExecutor` القديم. في `LangGraph`، يُتوقع من المطور استخدام أنماط المراقبة الحديثة بدلاً من الطباعة الفوضوية عبر `verbose=True`:
1. تمرير `debug=True` لطباعة انتقالات العقد وتحديثات الحالة لحظياً.
2. استدعاء `agent.stream(..., stream_mode="updates")` لتدفق المخرجات عقدة بعقدة.
3. تفعيل التتبع السحابي عبر **`LangSmith`** لتسجيل كافة المسارات وحساب استهلاك التوكنز والزمن لكل أداة.

### س2: كيف تصمم `Docstring` احترافية لأداة وكيل ذكاء اصطناعي في بيئة إنتاجية معقدة تضم عشرات الأدوات المتشابهة؟
**الإجابة النموذجية:**
الـ `Docstring` هي واجهة الاستخدام الموجهة للـ LLM (`LLM-Facing API`). لتجنب الخلط بين الأدوات:
1. نبدأ بجملة أمرية حاسمة توضح **متى تُستخدم الأداة ومتى لا تُستخدم** (مثلاً: *"Use ONLY for real-time weather lookups; do NOT use for historical climate averages."*).
2. نوثق كل معامل (`Args`) بصيغة واضحة، مع ذكر الصيغة المطلوبة (مثل: *"city: Full English city name without abbreviations, e.g., 'New York'"*).
3. نستخدم `Annotated` أو `Pydantic Field` لتعزيز التحقق من صحة المدخلات قبل وصولها للدالة الفعلية.

</div>
