# المرحلة العاشرة: أساسيات LangGraph والأنظمة متعددة الوكلاء المعتمدة على الحالة (LangGraph Fundamentals & Stateful Multi-Actor Systems)

مرحباً بك في **المرحلة العاشرة (Stage 10)** من مسار **RAG-Mastery**. تركز هذه المرحلة على الانتقال الجذري من السلاسل الخطية (`Linear Chains`) إلى **الرسوم البيانية الموجهة التكرارية (`Cyclic Stateful Graphs`)** باستخدام إطار العمل الرائد **`LangGraph`**.

---

## 🧭 خريطة المحاضرات في هذه المرحلة (Lectures Roadmap)

| رقم المحاضرة | عنوان المحاضرة | الدليل النظري والمعماري | الكود المرجعي (`stages/`) | المعمل التفاعلي (`playground/`) | الحالة |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **68** | مقدمة LangGraph وهندسة النظم المعتمدة على الحالة (Stateful Multi-Actor Systems, Pregel, Checkpointing, HITL) | [`01-langgraph-foundations-master-guide.md`](./01-langgraph-foundations-master-guide.md) | [`01-langgraph-introduction.ipynb`](../../stages/10-langgraph-fundamentals/01-langgraph-introduction/01-langgraph-introduction.ipynb) | [`01-langgraph-introduction.ipynb`](../../playground/10-langgraph-fundamentals/01-langgraph-introduction.ipynb) | مكتمل |
| **69** | إعداد بيئة عمل LangGraph وهندسة المراقبة والتتبع (Prefix Environments, VS Code Kernel, Secrets & Telemetry) | [`02-langgraph-environment-and-telemetry-master-guide.md`](./02-langgraph-environment-and-telemetry-master-guide.md) | [`02-environment-and-workspace-setup.ipynb`](../../stages/10-langgraph-fundamentals/02-environment-and-workspace-setup/02-environment-and-workspace-setup.ipynb) | [`02-environment-and-workspace-setup.ipynb`](../../playground/10-langgraph-fundamentals/02-environment-and-workspace-setup.ipynb) | مكتمل |
| **70 - 72** | مزودات الاستدلال، معمارية LPU، والتتبع عبر LangSmith (OpenAI, Groq LPU Economics, LangSmith Observability) | [`03-providers-and-telemetry-master-guide.md`](./03-providers-and-telemetry-master-guide.md) | [`03-providers-and-telemetry-setup.ipynb`](../../stages/10-langgraph-fundamentals/03-providers-and-telemetry-setup/03-providers-and-telemetry-setup.ipynb) | [`03-providers-and-telemetry-setup.ipynb`](../../playground/10-langgraph-fundamentals/03-providers-and-telemetry-setup.ipynb) | مكتمل |

---

## 🎯 الأهداف المعمارية والعملية للمرحلة العاشرة
1. **فهم نموذج الحوسبة التزامنية الفائقة (Bulk Synchronous Parallel - BSP)** المستوحى من نظام `Google Pregel` و `Apache Beam`.
2. **التحول من الـ DAG إلى الرسوم البيانية الدائرية (`Cyclic Graphs`)**: تمكين حلقات الاسترجاع التكراري، التفكير الذاتي (`Self-Reflection`)، ومعالجة الأخطاء.
3. **إدارة الحالة المشتركة (`State Management & Reducers`)**: هيكلة بيانات الحالة وضمان تحديثها الآمن عبر عقد الجراف دون تضارب.
4. **نقاط التفتيش والذاكرة المستمرة (`Checkpointing & Time Travel`)**: تسجيل لقطات الحالة (`Snapshots`) بعد كل خطوة لتوفير استمرارية الجلسات والتراجع الزمني.
5. **التدخل البشري في حلقة التنفيذ (`Human-in-the-Loop - HITL`)**: إيقاف الجراف عند نقاط محددة للموافقة البشرية وتعديل الحالة قبل الاستئناف.
