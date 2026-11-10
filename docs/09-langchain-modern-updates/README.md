<div dir="rtl">

# 09 - تحديثات LangChain الحديثة وبناء الوكلاء (LangChain v1+ Modern Ecosystem)
### Comprehensive Architectural Guide (`docs/09-langchain-modern-updates/`)

المرحلة التاسعة في مسار إتقان الـ RAG والـ Agentic AI، وتركز على تحديثات الجيل الأول الحديث (`LangChain v1+`)، وإدارة بيئات المشاريع عبر مدير الحزم السريع **`uv`**، وبناء الوكلاء الموحدين، والمخرجات المهيكلة، وبنية الـ Middleware.

---

## الدليل المعماري الموحد للمرحلة (Master Guide)

📄 **[الدليل الشامل: تحديثات LangChain الحديثة وبيئة التطوير السريعة (01-langchain-v1-ecosystem-master-guide.md)](./01-langchain-v1-ecosystem-master-guide.md)**
* **المحاضرات المشمولة**: المحاضرتان 57 و 58 (تحديثات LangChain v1+ وتأسيس بيئة UV والمفاتيح).
* **المحتوى العلمي الموحد**:
  * التحول المعماري من سلاسل `LangChain 0.x` التقليدية إلى معمارية الوكلاء الموحدة (`create_agent`) ومحرك `LangGraph`.
  * المحاور الثمانية الجديدة: `init_chat_model`، الوكلاء الموحدين، الأدوات (`@tool`)، المخرجات المهيكلة (`Pydantic`)، أنواع الرسائل، الذاكرة القصيرة، البث اللحظي، والبرمجيات الوسيطة (`Middlewares`).
  * تشريح بنية الـ **Middleware** المدمجة والمخصصة (`AgentMiddleware`, `HumanInTheLoopMiddleware`).
  * مدير الحزم السريع **`uv`** ودورة التأسيس الكاملة (`uv init`, `uv venv`, `.venv` activation, `uv add -r`, `ipykernel`).
  * حوكمة مفاتيح الـ API عبر `.env` و `.gitignore` لمزودي الخدمة (`Google Gemini`, `Groq`, `OpenAI`).
  * بيئات التطوير الوكالية الحديثة (`Agentic IDEs: Google Antigravity, Cursor, VS Code`).
  * أسئلة المقابلات المتقدمة للـ Senior AI Engineers.

---

## فهرس المشاريع البرمجية التابعة للمرحلة

| الرقم | عنوان الموضوع البرمجي | المحاضرة المقابلة | الكود المرجعي (`stages/`) | معمل التجربة (`playground/`) | الحالة |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 01 | **استكشاف منظومة LangChain v1+ وإعداد بيئة UV** | Lecture 57 | [`01-langchain-uv-setup-and-ecosystem.ipynb`](../../stages/09-langchain-modern-updates/01-langchain-uv-setup-and-ecosystem/01-langchain-uv-setup-and-ecosystem.ipynb) | [`01-langchain-uv-setup-and-ecosystem.ipynb`](../../playground/09-langchain-modern-updates/01-langchain-uv-setup-and-ecosystem.ipynb) | مكتمل |
| 02 | **تأسيس البيئة الافتراضية وحوكمة المكتبات والمفاتيح بـ UV** | Lecture 58 | [`02-uv-environment-and-keys-setup.ipynb`](../../stages/09-langchain-modern-updates/02-uv-environment-and-keys-setup/02-uv-environment-and-keys-setup.ipynb) | [`02-uv-environment-and-keys-setup.ipynb`](../../playground/09-langchain-modern-updates/02-uv-environment-and-keys-setup.ipynb) | مكتمل |

---

## المعايير الهندسية للمرحلة
* **`stages/`**: كود إنتاجي Senior مسبق التنفيذ بمخرجاته الكاملة، بتوثيق إنجليزي فني صارم وخالٍ من الرموز التعبيرية مع فحوصات `Assertions`.
* **`playground/`**: كشكول تجارب تفاعلي ودود باللغة العربية البسيطة يتيح التجربة الحرة وتعديل المعاملات والمسارات دون قيود.
* **`docs/`**: دليل معماري موحد وفائق الدقة يجمع النظرية والرياضيات والأنظمة في مرجع شامل متماسك.

</div>
