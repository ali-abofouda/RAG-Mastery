# 01 - معالجة وإدخال البيانات (Data Ingestion & Parsing Techniques)

المرحلة الأولى في رحلة التطبيق العملي لأنظمة الـ RAG، وتركز على كيفية استيراد وتحليل وتجزئة مختلف أنواع ومصادر البيانات لتحويلها إلى صيغة قابلة للتضمين والبحث.

---

## 🧪 مساحة التجارب والمعمل العملي (Playground & Lab)

كافة التجارب التراكمية والأكواد العملية للقسم مجمعة في معمل تجارب مركزي:
* 📁 **[playGround/](./playGround/)**:
  * 📓 **[`playground.ipynb`](./playGround/playground.ipynb)**: دفتر التجارب الحرة لتطبيق واختبار أكواد الـ Ingestion.
  * 📂 **[`data/`](./playGround/data/)**: مجلد يحوي ملفات البيانات التجريبية (`artificial_intelligence.txt`، `software_engineering.txt`، `web_development.txt`).

---

## فهرس موضوعات ومراجع القسم (Reference Curriculum)

المجلدات الفرعية مصممة كمراجع منظمة ونظيفة تحوي:
* **الدليل الشارح (`README.md`):** توثيق نظري وهندسي شامل للدرس ومخططات توضيحية.
* **دفتر الملاحظات المرجعي (`.ipynb`):** كود الدرس النموذجي ومسبوق بخلايا Markdown شارحة.

| الرقم | المجلد الفرعي | الموضوع (Topic) | الشرح (.md) | الدفتر المرجعي (.ipynb) | الحالة |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 01 | **[01-environment-setup](./01-environment-setup/)** | إعداد بيئة العمل وهيكل المشروع باستخدام UV | [README](./01-environment-setup/README.md) | [Notebook](./01-environment-setup/01-environment-setup.ipynb) | [x] مكتمل |
| 02 | **[02-document-structure](./02-document-structure/)** | بنية كائن الـ Document والميتا-داتا في LangChain | [README](./02-document-structure/README.md) | [Notebook](./02-document-structure/02-document-structure.ipynb) | [x] مكتمل |
| 03 | **[03-text-loaders](./03-text-loaders/)** | قراءة وتحليل الملفات النصية باستخدام Document Loaders | [README](./03-text-loaders/README.md) | [Notebook](./03-text-loaders/03-text-loaders.ipynb) | [x] مكتمل |
| 04 | **[04-text-splitting](./04-text-splitting/)** | تقنيات واستراتيجيات تجزئة النصوص (Text Splitting) | [README](./04-text-splitting/README.md) | [Notebook](./04-text-splitting/04-text-splitting.ipynb) | [x] مكتمل |
| 05 | **[05-pdf-parsing](./05-pdf-parsing/)** | قراءة واستخراج مستندات الـ PDF | [README](./05-pdf-parsing/) | - | [ ] قيد البدء |
| 06 | **[06-pdf-advanced-issues](./06-pdf-advanced-issues/)** | حل المشكلات المعقدة في الـ PDF (جداول، تنسيقات) | [README](./06-pdf-advanced-issues/) | - | [ ] قيد البدء |
| 07 | **[07-word-documents](./07-word-documents/)** | قراءة وتحليل مستندات Word (DOCX) | [README](./07-word-documents/) | - | [ ] قيد البدء |
| 08 | **[08-csv-excel](./08-csv-excel/)** | معالجة ملفات الجداول CSV و Excel | [README](./08-csv-excel/) | - | [ ] قيد البدء |
| 09 | **[09-json-processing](./09-json-processing/)** | قراءة وتحليل بيانات JSON المهيكلة | [README](./09-json-processing/) | - | [ ] قيد البدء |
| 10 | **[10-sql-databases](./10-sql-databases/)** | ربط واستخراج البيانات من قواعد بيانات SQL | [README](./10-sql-databases/) | - | [ ] قيد البدء |

---

## قواعد عمل الـ Agent:
* 🤖 **[agent.md](./agent.md)**: القواعد والضوابط المنظمة ومسؤولية تنظيم الـ Playground عند الطلب.
