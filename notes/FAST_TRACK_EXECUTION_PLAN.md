# خطة الـ 2 ساعة يومياً المزدوجة: الكورس + المشاريع المؤسسية بالتوازي
### (The Dual-Track Mastery Plan: Course & Production Engineering)

> **المبدأ:** ساعتان يومياً مقسمة بانتظام: **[ساعة لاستيعاب معمارية الكورس] + [ساعة للتطبيق البرمجي المباشر في مشروع الـ HR]**.
> **المرونة الزمنية:** الخطة مصممة على **11 يوماً أساسياً + 3 أيام مرونة واحتياط (Buffer Days)**، بما يسمح بإنهاء كل شيء بأريحية تامة وبدون أي ضغط حتى مطلع الشهر.

---

## ⏱️ الميزانية الزمنية اليومية (Daily 2-Hour Time Budget)

* **الساعة الأولى (من 50 إلى 60 دقيقة): مسار الكورس والمعمارية (Track 1):**
  - مشاهدة من 4 إلى 5 محاضرات بتركيز على سرعة `1.25x`.
  - استيعاب المفاهيم الهندسية، أشكال الـ State، والتفرعات الشرطية في LangGraph بدون تضييع وقت في كتابة الكود النظري يدوياً.
* **الساعة الثانية (60 دقيقة): مسار التطبيق في المشروع (Track 2):**
  - فتح نافذة مشروع `HR Policy RAG Assistant`.
  - تطبيق المعمارية المشروحة فوراً في كود بايثون واختباره وتوصيله بالـ UI وقاعدة البيانات Qdrant.

---

## 🗓️ جدول التنفيذ اليومي التفصيلي الموزع (مع التوقيتات والمخرجات)

| اليوم والتاريخ | ساعة الكورس (المحاضرات ووقت الفيديو 1.25x) | ساعة المشروع (التطبيق العملي الموازي في HR Assistant) | إجمالي الوقت اليومي | المخرجات الهندسية اليومية |
| :---: | :--- | :--- | :---: | :--- |
| **اليوم 01**<br>(الخميس 19 نوفمبر) | **محاضرات 76–79:** (~ 48 دقيقة)<br>- `State Schema With Data Classes`<br>- `Pydantic Data Validation`<br>- `Complex State Management`<br>- `Intro To Router In LangGraph` | **تأسيس حالة الوكيل (Agent State):** (~ 60 دقيقة)<br>بناء ملف `agent_state.py` باستخدام Pydantic لتعريف حالة المحادثة، الأسئلة السابقة، ورسائل الذاكرة. | **~ ساعتان** | هيكل بيانات الـ Agent جاهز ونظيف بـ Type Safety. |
| **اليوم 02**<br>(الجمعة 20 نوفمبر) | **محاضرات 80–83:** (~ 52 دقيقة)<br>- `Conditional Edges`<br>- `Multiple Routing Options`<br>- `Tool Calling Setup`<br>- `Binding Tools to LLMs` | **بناء مسارات التوجيه (Router Node):** (~ 60 دقيقة)<br>برمجة عقدة التوجيه الشرطي لتحديد هل السؤال يخص سياسات الـ HR أم استفسار عام/خارج السياق. | **~ ساعتان** | الـ Agent قادر على فلترة وتوجيه السؤال تلقائياً. |
| **اليوم 03**<br>(السبت 21 نوفمبر) | **محاضرات 84–86:** (~ 50 دقيقة)<br>- `ToolNode Architecture`<br>- `Handling Tool Execution`<br>- `ReAct Agent Foundation` | **تحويل محرك البحث لأداة (Retriever Tool):** (~ 60 دقيقة)<br>تحويل محرك Qdrant Hybrid Search لأداة مسجلة في LangGraph وربطها بـ `ToolNode`. | **~ ساعتان** | الوكيل يستدعي محرك استرجاع السياسات كأداة ذكية. |
| **اليوم 04**<br>(الأحد 22 نوفمبر) | **محاضرات 87–89:** (~ 50 دقيقة)<br>- `Building Full ReAct Agent`<br>- `State Reducers for Chat`<br>- `Streaming Output Tokens` | **تكامل واجهة Streamlit وبث الردود:** (~ 60 دقيقة)<br>ربط LangGraph StateGraph بواجهة Streamlit وتشغيل الـ Streaming الحي للتوكنز. | **~ ساعتان** | **اكتمال Phase 2 بالكامل:** نظام محادثة تفاعلي متصل بالـ UI. |
| **اليوم 05**<br>(الإثنين 23 نوفمبر) | **محاضرات 90–93:** (~ 52 دقيقة)<br>- `Traditional vs Agentic RAG`<br>- `Query Planning Foundations`<br>- `Sub-query Generation` | **إعادة صياغة الأسئلة (Query Rewriting):** (~ 60 دقيقة)<br>إضافة عقدة تعيد صياغة الأسئلة التتابعية المبهمة (Follow-ups) بناءً على سياق المحادثة. | **~ ساعتان** | حل مشكلة الأسئلة الناقصة مثل *"طب وبالنسبة للإجازة المرضية؟"*. |
| **اليوم 06**<br>(الثلاثاء 24 نوفمبر) | **محاضرات 94–98:** (~ 55 دقيقة)<br>- `Self-Reflection Nodes`<br>- `Answer Groundedness Check`<br>- `Multi-Agent Supervisor Concept` | **فحص الهلوسة الذاتي (Hallucination Checker):** (~ 60 دقيقة)<br>إضافة عقدة فحص ذاتي تتأكد أن الإجابة مستندة 100% لنصوص سياسات الشركة. | **~ ساعتان** | منع النظام من اختراع أي سياسة غير موجودة. |
| **اليوم 07**<br>(الأربعاء 25 نوفمبر) | **محاضرات 99–105:** (~ 50 دقيقة)<br>- `Autonomous Workflows`<br>- `Supervisor State Routing`<br>- (تصفح سريع للفكرة المعمارية) | **تنظيم وتحسين استدعاءات الـ APIs:** (~ 60 دقيقة)<br>تنظيف استدعاءات Groq/OpenAI وضبط التكلفة والـ Fallback في حالة الخطأ. | **~ ساعتان** | كود مرن ومحصن ضد انقطاع أي Model Provider. |
| **اليوم 08**<br>(الخميس 26 نوفمبر) | **محاضرات 106–109:** (~ 48 دقيقة)<br>- `Corrective RAG (CRAG)`<br>- `Document Relevance Evaluator`<br>- `Adaptive RAG Routing` | **تقييم المستندات (Document Relevance Grader):** (~ 60 دقيقة)<br>برمجة عقدة تقييم جودة الـ Chunks المسترجعة؛ لو غير مفيدة يلجأ لمسار بديل أو يطلب توضيحاً. | **~ ساعتان** | نظام استرجاع تصحيحي CRAG مدمج داخل المشروع. |
| **اليوم 09**<br>(الجمعة 27 نوفمبر) | **محاضرات 110–114:** (~ 55 دقيقة)<br>- `Persistent Memory & Checkpointers`<br>- `SqliteSaver vs PostgresSaver`<br>- `Vectorless RAG Concepts` | **حفظ الجلسات المستمرة (Memory Persistence):** (~ 60 دقيقة)<br>دمج `SqliteSaver` أو `PostgresSaver` في LangGraph لحفظ جلسات المستخدم بين كل ريفريش. | **~ ساعتان** | ذاكرة دائمة للمحادثات لكل موظف عبر Session ID. |
| **اليوم 10**<br>(السبت 28 نوفمبر) | **محاضرات 115–118:** (~ 45 دقيقة)<br>- `Guardrails in RAG`<br>- `LLM Gateways Architecture`<br>- `Intro to Evaluation Metrics` | **درع الأمان المؤسسي (Security Guardrails):** (~ 60 دقيقة)<br>إضافة فلاتر فحص الـ Prompt Injection ومنع تسريب بيانات الرواتب الحساسة. | **~ ساعتان** | نظام مؤمن بالكامل بمستوى Enterprise Security. |
| **اليوم 11**<br>(الأحد 29 نوفمبر) | **محاضرات 119–122:** (~ 55 دقيقة)<br>- `RAG Evaluation with Ragas`<br>- `Faithfulness & Answer Relevance`<br>- `LLM-as-a-Judge Automation` | **بناء سويت التقييم الآلي (Automated Evals):** (~ 60 دقيقة)<br>كتابة سكريبت اختبار آلي بـ Ragas لحساب درجات: `Faithfulness`, `Answer Relevance`, و `Context Precision`. | **~ ساعتان** | تقرير أداء رقمي ومقاييس حقيقية تضاف للـ CV. |

---

## 🛡️ منطقة الأمان والمرونة الزمنية (The Flex & Buffer Window)

* **اليوم 12 (الإثنين 30 نوفمبر):** يوم مرونة (Flex Day 1) — مخصص لتدارك أي تأخير، أو إنهاء أي تفصيلة تقنية في كود مشروع الـ HR.
* **اليوم 13 (الثلاثاء 01 ديسمبر):** يوم مرونة (Flex Day 2) — كتابة الـ Dockerfile واختبار تشغيل المشروع في حاوية Docker محلية والتأكد من استقرار الـ Streamlit UI.
* **اليوم 14 (الأربعاء 02 ديسمبر):** يوم التوثيق النهائي (Release Day) — تحديث README مشروع الـ HR، وعمل Tag Release على GitHub، وتحديث الـ CV بروابط المشروع.

---

## 🎯 المحطة الكبرى التالية (The Ultimate Next Step)
بنهاية هذه الخطة المريحة، تصبح جاهزاً 100% لخوض:
**Section 31 & 32: AI Forward Deployed Engineer (AI FDE) Enterprise Platform**
(مشروع متجر التجارة الإلكترونية السحابي على Google Cloud Platform مع MongoDB والأنظمة القديمة).
