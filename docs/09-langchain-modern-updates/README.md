<div dir="rtl">

# 09 - تحديثات LangChain الحديثة وبناء الوكلاء (LangChain v1+ Modern Ecosystem)
### Comprehensive Architectural Guide (`docs/09-langchain-modern-updates/`)

المرحلة التاسعة في مسار إتقان الـ RAG والـ Agentic AI، وتركز على تحديثات الجيل الأول الحديث (`LangChain v1+`)، وإدارة بيئات المشاريع عبر مدير الحزم السريع **`uv`**، وبناء الوكلاء الموحدين، والمخرجات المهيكلة، وبنية الـ Middleware.

---

## الأدلة المعمارية الموحدة للمرحلة (Master Guides)

1. 📄 **[الدليل الشامل 01: تحديثات LangChain الحديثة وبيئة التطوير السريعة (01-langchain-v1-ecosystem-master-guide.md)](./01-langchain-v1-ecosystem-master-guide.md)** *(المحاضرات 57 و 58)*
   * التحول المعماري من سلاسل `LangChain 0.x` إلى `LangChain v1+`، بنية الـ `Middleware`، ومدير الحزم السريع `uv` وحوكمة مفاتيح الـ API.

2. 📄 **[الدليل الشامل 02: بناء الوكلاء الموحدين واستدعاء الأدوات في LangChain v1+ (02-unified-agents-and-tool-calling-master-guide.md)](./02-unified-agents-and-tool-calling-master-guide.md)** *(المحاضرة 59)*
   * قيد انقطاع التدريب (`Cutoff Date`)، دالة `create_agent`، تطور طوبولوجيا الرسم البياني (`START -> model <-> tools -> END`)، عقد التوجيه عبر `Docstring`، وتتبع مسار الرسائل الأربعة (`Human -> AI ToolCall -> Tool -> AI Final`).

---

## فهرس المشاريع البرمجية التابعة للمرحلة

| الرقم | عنوان الموضوع البرمجي | المحاضرة المقابلة | الكود المرجعي (`stages/`) | معمل التجربة (`playground/`) | الحالة |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 01 | **استكشاف منظومة LangChain v1+ وإعداد بيئة UV** | Lecture 57 | [`01-langchain-uv-setup-and-ecosystem.ipynb`](../../stages/09-langchain-modern-updates/01-langchain-uv-setup-and-ecosystem/01-langchain-uv-setup-and-ecosystem.ipynb) | [`01-langchain-uv-setup-and-ecosystem.ipynb`](../../playground/09-langchain-modern-updates/01-langchain-uv-setup-and-ecosystem.ipynb) | مكتمل |
| 02 | **تأسيس البيئة الافتراضية وحوكمة المكتبات والمفاتيح بـ UV** | Lecture 58 | [`02-uv-environment-and-keys-setup.ipynb`](../../stages/09-langchain-modern-updates/02-uv-environment-and-keys-setup/02-uv-environment-and-keys-setup.ipynb) | [`02-uv-environment-and-keys-setup.ipynb`](../../playground/09-langchain-modern-updates/02-uv-environment-and-keys-setup.ipynb) | مكتمل |
| 03 | **بناء أول وكيل موحد واستدعاء الأدوات عبر `create_agent`** | Lecture 59 | [`03-creating-first-unified-agent.ipynb`](../../stages/09-langchain-modern-updates/03-creating-first-unified-agent/03-creating-first-unified-agent.ipynb) | [`03-creating-first-unified-agent.ipynb`](../../playground/09-langchain-modern-updates/03-creating-first-unified-agent.ipynb) | مكتمل |

---

## المعايير الهندسية للمرحلة
* **`stages/`**: كود إنتاجي Senior مسبق التنفيذ بمخرجاته الكاملة، بتوثيق إنجليزي فني صارم وخالٍ من الرموز التعبيرية مع فحوصات `Assertions`.
* **`playground/`**: كشكول تجارب تفاعلي ودود باللغة العربية البسيطة يتيح التجربة الحرة وتعديل المعاملات والمسارات دون قيود.
* **`docs/`**: دليل معماري موحد وفائق الدقة يجمع النظرية والرياضيات والأنظمة في مرجع شامل متماسك.

</div>
