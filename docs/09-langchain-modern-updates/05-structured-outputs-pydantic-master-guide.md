<div dir="rtl">

# الدليل المعماري الشامل: المخرجات المهيكلة (`Pydantic` مقابل `TypedDict`) وفحص قدرات النماذج (`model.profile`)
### Schema Enforcement, `Field` Validation, `TypedDict` with `Annotated`, `include_raw=True`, and Capability Introspection (Lectures 63 - 64)

---

## 1. الدافع الهندسي: لماذا تفشل النصوص الحرة في الأنظمة الإنتاجية؟

عندما تطلب من نموذج لغوي عادي (`Plain LLM`) تلخيص تفاصيل فيلم أو استخراج بيانات عميل عبر `model.invoke("Provide details about Inception")`:
* سيعيد النموذج نصاً أدبياً حراً ومتغيراً في كل مرة.
* إذا أرادت قاعدة بيانات أو واجهة `REST API` أو خط أنابيب بيانات (`Data Pipeline`) قراءة "السنة" كرقم صحيح (`int`) و"التقييم" كرقم عشري (`float`)، فسيكون تحليل النص الحر (`Regex Parsing`) هشاً وينهار عند أي تغير في صياغة النموذج.

**الحل المعماري — المخرجات المهيكلة (`Structured Outputs`)**:
إلزام النموذج اللغوي بإخراج استجابة تطابق مخطط بيانات برمجي صارم (`Schema Enforcement`) عبر دالة **`model.with_structured_output(Schema)`**.

</div>

```mermaid
flowchart LR
    PyClass["تعريف كلاس Pydantic<br>(Movie / MovieDetails)"] -->|"JSON Schema Auto-Gen"| Bind["ربط المخطط بالنموذج<br>model.with_structured_output(Movie)"]
    Prompt["سؤال المستخدم: تفاصيل فيلم Inception"] --> Bind
    Bind --> LLM["خادم النموذج اللغوي (Tool/JSON Constraining)"]
    LLM -->|"JSON منضبط"| Validate{"محرك تحقق Pydantic"}
    Validate -->|"الأنواع صحيحة 100%"| ValidObj["كائن بايثون جاهز للوصول المباشر:<br>res.title, res.year, res.rating"]
    Validate -->|"نوع خاطئ أو حقل ناقص"| Err["إطلاق ValidationError / parsing_error"]
```

<div dir="rtl">

---

## 2. ثلاث ركائز لـ `Pydantic` (`BaseModel` + `Field`)

تدعم `LangChain` ثلاثة قوالب لهيكلة المخرجات (`Pydantic`, `TypedDict`, `Dataclasses`)، ويتربع **`Pydantic`** على القمة الإنتاجية بفضل ثلاث ميزات حاسمة:

1. **التحقق الفوري للأنواع (`Runtime Field Validation`)**:
   * يضمن أن حقل `title` نص (`str`)، وحقل `year` رقم صحيح (`int`)، وحقل `rating` عشري (`float`). إذا أعاد النموذج نصاً مكان الرقم أو العكس، يكتشفه `Pydantic` فوراً ولا يسمح بتسرب بيانات تالفة لقاعدة البيانات.
2. **الأوصاف الموجهة للنموذج (`LLM-Facing Field Descriptions`)**:
   * تمرير `Field(..., description="...")` يغذي النموذج بتعليمات دقيقة حول معنى كل حقل وصيغته المتوقعة.
   * **ملاحظة هندسية مهمة**: عند طلب أرقام ذات وحدات قياس (مثل الميزانية بالمليون دولار)، يجب صياغة الوصف بوضوح مثل: `"Budget expressed in millions of USD (e.g., write 160.0 for $160 million)"`؛ لأن الوصف العام `"Budget in millions USD"` قد يدفع النموذج أحياناً لكتابة `160000000.0` بدلاً من `160.0`.
3. **الهياكل المتداخلة (`Nested Schemas`)**:
   * دعم تعريف كلاس داخل قائمة في كلاس آخر (مثل قائمة ممثلين `List[Actor]` داخل `MovieDetails`).

```python
from pydantic import BaseModel, Field

class Movie(BaseModel):
    title: str = Field(..., description="The title of the movie")
    year: int = Field(..., description="The year the movie was released")
    director: str = Field(..., description="The director of the movie")
    rating: float = Field(..., description="The movie's rating out of 10")

model_with_structure = model.with_structured_output(Movie)
response = model_with_structure.invoke("Provide details about the movie Inception")
# المخرج كائن Movie مباشر: response.director == 'Christopher Nolan'
```

---

## 3. حفظ الرسالة الخام والبيانات الوصفية (`include_raw=True`)

عند استدعاء `model.with_structured_output(Movie)` افتراضياً، يُرجع الكائن المهيكل (`Movie`) فقط ويتم التخلص من رسالة `AIMessage` الأصلية، مما يضيع بيانات **`usage_metadata`** (استهلاك التوكنز والتكلفة).

لتفادي ذلك في الإنتاج، نمرر المعامل **`include_raw=True`**:
```python
model_with_raw = model.with_structured_output(Movie, include_raw=True)
result = model_with_raw.invoke("Provide details about the movie Inception")
```
يُرجع هذا الاستدعاء قاموساً يضم 3 مفاتيح استراتيجية:
1. **`result["raw"]`**: كائن `AIMessage` الأصلي كاملاً (يحمل `usage_metadata`، الـ ID، وبيانات التتبع).
2. **`result["parsed"]`**: كائن `Movie` المهيكل بعد نجاح التحقق (أو `None` عند الفشل).
3. **`result["parsing_error"]`**: قيمة `None` عند النجاح، أو استثناء الخطأ الدقيق عند فشل التحليل؛ مما يمنع انهيار التطبيق (`Graceful Degradation`).

---

## 4. الهياكل المتداخلة المعقدة (`Nested Pydantic Structures`)

عند استخراج وثائق مؤسسية (مثل الفواتير التي تضم قائمة بنود، أو ملفات الأفلام التي تضم طاقم عمل متعدد):

```python
from typing import List, Optional

class Actor(BaseModel):
    name: str
    role: str

class MovieDetails(BaseModel):
    title: str
    year: int
    cast: List[Actor]  # هيكل متداخل: قائمة كائنات من نوع Actor
    genres: List[str]
    budget: Optional[float] = Field(None, description="Budget in millions USD (e.g. 160.0)")
```

---

## 5. البديل الخفيف بدون تحقق وقت التشغيل: `TypedDict` و `Annotated` (`Lecture 64`)

عندما لا يحتاج تطبيقك إلى فحص صارم للأنواع أثناء وقت التشغيل (`Runtime Validation`) وترغب في التعامل مع قاموس بايثون قياسي خفيف (`Plain dict`)، يوفر **`TypedDict`** مع **`Annotated`** بديلاً ممتازاً باستخدام نظام الأنواع المدمج في بايثون:

```python
from typing_extensions import TypedDict, Annotated
from typing import List, Optional

class MovieDict(TypedDict):
    title: Annotated[str, ..., "The title of the movie"]
    year: Annotated[int, ..., "The year the movie was released"]
    director: Annotated[str, ..., "The director of the movie"]
    rating: Annotated[float, ..., "The movie's rating out of 10"]

model_with_typedict = model.with_structured_output(MovieDict)
response = model_with_typedict.invoke("Provide details about the movie Avengers")
# المخرج قاموس بايثون عادي: {'director': 'Joss Whedon', 'rating': 8, 'title': 'The Avengers', 'year': 2012}
```

### الهياكل المتداخلة عبر `TypedDict`:
تماماً مثل `Pydantic`، يدعم `TypedDict` تداخل القواميس (مثل `ActorDict` داخل `MovieDetailsDict`) مع الاستمرار في إرجاع قواميس قياسية دون إطلاق `ValidationError` إذا تغير نوع حقل فرعي:
```python
class ActorDict(TypedDict):
    name: Annotated[str, ..., "Actor full name"]
    role: Annotated[str, ..., "Role played"]

class MovieDetailsDict(TypedDict):
    title: Annotated[str, ..., "Movie title"]
    cast: Annotated[List[ActorDict], ..., "Top cast members"]
```

---

## 6. فحص قدرات النموذج برمجياً عبر `model.profile` في `LangChain v1+`

تتيح ميزة **`model.profile`** الحديثة استكشاف المواصفات والقدرات الفعلية للنموذج اللغوي قبل ربطه بأدوات أو وسائط متعددة:

* **تنبيه هندسي هام**: استدعاء `.profile` على النموذج الملفوف `model_with_structured_output.profile` سيطلق خطأ:  
  `AttributeError: 'RunnableSequence' object has no attribute 'profile'`؛ لأن `with_structured_output()` يغلف النموذج داخل تسلسل تنفيذ `RunnableSequence`.
* يجب دائماً استدعاء `model.profile` على **كائن النموذج الأساسي (`BaseChatModel`)** مباشرة:

```python
print(model.profile)
# المخرج الفعلي لنموذج ChatGroq (openai/gpt-oss-20b):
# {
#   'name': 'GPT OSS 20B',
#   'max_input_tokens': 131072,
#   'max_output_tokens': 65536,
#   'text_inputs': True, 'image_inputs': False, 'audio_inputs': False,
#   'reasoning_output': True, 'tool_calling': True, 'structured_output': True
# }
```

> **الفائدة الإنتاجية**: تستطيع بكتابة دالة فحص واحدة في بداية تشغيل الوكيل التحقق مما إذا كان النموذج يدعم `structured_output: True` و `tool_calling: True` و `image_inputs` تلقائياً قبل إرسال أي طلبات سحابية!

---

## 7. مصفوفة المفاضلة الهندسية الشاملة (`Pydantic` مقابل `TypedDict`)

| المعيار الهندسي | `Pydantic BaseModel` | `TypedDict + Annotated` |
| :--- | :--- | :--- |
| **نوع المخرج البرمجي** | كائن كلاس منظم (`res.title`, `res.year`). | قاموس بايثون قياسي (`res["title"]`, `res["year"]`). |
| **التحقق في وقت التشغيل (`Runtime Validation`)** | **صارم جداً** (يرفض القيم المخالفة ويطلق `ValidationError`). | **لا يوجد** (مجرد تلميحات أنواع؛ القاموس يقبل أي قيمة في Runtime). |
| **تمرير وصف الحقول للـ LLM** | عبر `Field(..., description="...")`. | عبر `Annotated[type, ..., "description"]`. |
| **العبء الحسابي (`Overhead`)** | عبء طفيف بسبب تشغيل محرك التحقق في Rust/Pydantic v2. | صفر عبء تقريباً (`Native dict`). |
| **حالات الاستخدام الأنسب** | **أنظمة الإنتاج الحرجة**، واجهات FastAPI، وقواعد البيانات الصارمة. | النماذج الأولية السريعة (`Prototyping`) وتدفقات الحالة الداخلية في LangGraph. |

---

## 8. أسئلة المقابلات المتقدمة للـ Senior AI Engineers

### س1: كيف تعمل دالة `with_structured_output()` داخلياً مع مزودي النماذج مثل OpenAI و Groq؟
**الإجابة النموذجية:**
تستخدم `with_structured_output` إحدى آليتين حسب قدرات النموذج ومزود الخدمة:
1. **Tool/Function Calling Method** (الوضع الافتراضي الشائع في Groq و نماذج LangChain): تحول `Pydantic` أو `TypedDict` إلى `JSON Schema` وتمرره للنموذج كـ أداة إلزامية، ثم تحلل الحجج (`tool_calls[0]["args"]`).
2. **Native JSON Schema (`json_schema` / Constrained Decoding)**: في أحدث النماذج مثل OpenAI GPT-4o، تفرض واجهة الـ API قيوداً على مستوى أخذ عينات التوكنز (`Logit Biasing / CFG`) تضمن هندسياً استحالة توليد رمز لا يتطابق مع المخطط بنسبة $100\%$.

### س2: لماذا يُعد استخدام `include_raw=True` إلزامياً في أنظمة الإنتاج المالية والطبية؟
**الإجابة النموذجية:**
لسببين معماريين جوهريين:
1. **مراقبة التكاليف والأداء (`FinOps & Observability`)**: بدون `include_raw=True` تفقد حقول `usage_metadata` فلا تستطيع حساب فاتورة التوكنز (بما فيها توكنز التفكير الخفية) لكل طلب استخراج.
2. **المرونة الدفاعية (`Defensive Error Handling`)**: عند فشل النموذج في مطابقة حقل صارم، يقوم وضع `include_raw=False` بإطلاق استثناء مباشر يكسر مسار التنفيذ. أما `include_raw=True` فيحتوي الخطأ داخل المفتاح `parsing_error` ويمنحك النص الخام `raw` لتتمكن من تمريره لحلقة تصحيح ذاتي (`Self-Correction Retry`)!

### س3: متى تفضل استخدام `TypedDict` على `Pydantic` في أنظمة LangGraph؟ ولماذا قد يفشل `.profile` بعد ربط المخطط؟
**الإجابة النموذجية:**
يُفضل **`TypedDict`** لتعريف كائن الحالة الداخلية المشتركة (`Graph State`) أو في خطوات المعالجة السريعة داخل العقد حيث لا ترغب في تكلفة تحويل الكائنات أو تقييد تحديثات القاموس؛ بينما يظل **`Pydantic`** إلزامياً عند حدود الإدخال/الإخراج الخارجية (`API Boundaries`).  
أما فشل `.profile` بعد استدعاء `with_structured_output()` فيحدث لأن الدالة لا تعيد `BaseChatModel`، بل تُنشئ تسلسلاً مركباً (`RunnableSequence`) يربط `[Model | Parser]`؛ لذلك يجب فحص `model.profile` على النموذج الأساسي قبل الربط للتحقق من دعم `structured_output` أو `image_inputs`.

</div>
