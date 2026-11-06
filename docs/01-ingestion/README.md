# المرحلة 01: معالجة واستيعاب البيانات (Data Ingestion & Parsing)
### Comprehensive Architectural Guide (`docs/01-ingestion/`)

المرحلة الأولى في رحلة التطبيق العملي لأنظمة الـ RAG، وتركز على كيفية استيراد وتحليل وتجزئة مختلف أنواع ومصادر البيانات لتحويلها إلى صيغة قابلة للتضمين والبحث الدلالي.

> **الدليل المرجعي الشامل للمرحلة (Master Guide):**  
> لقراءة التوثيق الهندسي والمعماري الكامل لكافة موضوعات المرحلة والمقارنات الإنتاجية بالتفصيل:  
> [STAGE_01_INGESTION_GUIDE.md](./STAGE_01_INGESTION_GUIDE.md)

---

## فهرس موضوعات ومشاريع المرحلة

| الرقم | عنوان المشروع البرمجي | المحاضرة المقابلة | الشرح المعماري (`docs/`) | الكود المرجعي (`stages/`) | معمل التجربة (`playground/`) | الحالة |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 01 | **إعداد بيئة العمل وهيكل المشروع باستخدام UV** | Lecture 08 | [الدليل الشامل](./STAGE_01_INGESTION_GUIDE.md#3-الدرس-01-إعداد-بيئة-العمل-والتحكم-في-الاعتماديات-01-environment-setup) | [`stages/01/.../01-...ipynb`](../../stages/01-ingestion/01-environment-setup/01-environment-setup.ipynb) | [`playground/01/.../01-...ipynb`](../../playground/01-ingestion/01-text-parsing.ipynb) | [x] مكتمل |
| 02 | **بنية كائن الـ Document في LangChain** | Lecture 09 | [الدليل الشامل](./STAGE_01_INGESTION_GUIDE.md#4-الدرس-02-بنية-كائن-المستند-وهندسة-البيانات-الوصفية-02-document-structure) | [`stages/01/.../02-...ipynb`](../../stages/01-ingestion/02-document-structure/02-document-structure.ipynb) | [`playground/01/.../01-...ipynb`](../../playground/01-ingestion/01-text-parsing.ipynb) | [x] مكتمل |
| 03 | **قراءة واستيراد الملفات النصية TextLoader** | Lecture 10 | [الدليل الشامل](./STAGE_01_INGESTION_GUIDE.md#5-الدرس-03-قراءة-الملفات-النصية-واستراتيجيات-الترميز-03-text-loaders) | [`stages/01/.../03-...ipynb`](../../stages/01-ingestion/03-text-loaders/03-text-loaders.ipynb) | [`playground/01/.../01-...ipynb`](../../playground/01-ingestion/01-text-parsing.ipynb) | [x] مكتمل |
| 04 | **استراتيجيات وتقنيات تجزئة النصوص Text Splitting** | Lecture 11 | [الدليل الشامل](./STAGE_01_INGESTION_GUIDE.md#6-الدرس-04-تقنيات-تجزئة-وتقطيع-النصوص-04-text-splitting) | [`stages/01/.../04-...ipynb`](../../stages/01-ingestion/04-text-splitting/04-text-splitting.ipynb) | [`playground/01/.../01-...ipynb`](../../playground/01-ingestion/01-text-parsing.ipynb) | [x] مكتمل |
| 05 | **قراءة واستخراج مستندات PDF في LangChain** | Lecture 12 | [الدليل الشامل](./STAGE_01_INGESTION_GUIDE.md#7-الدرس-05-أساسيات-قراءة-ومقارنة-محملات-pdf-05-pdf-parsing) | [`stages/01/.../05-...ipynb`](../../stages/01-ingestion/05-pdf-parsing/05-pdf-parsing.ipynb) | [`playground/01/.../02-...ipynb`](../../playground/01-ingestion/02-pdf-parsing.ipynb) | [x] مكتمل |
| 06 | **حل المشكلات المعقدة في الـ PDF وتنظيف النصوص** | Lecture 13 | [الدليل الشامل](./STAGE_01_INGESTION_GUIDE.md#8-الدرس-06-معالجة-مشكلات-pdf-المعقدة-والخط-الإنتاجي-06-pdf-advanced-issues) | [`stages/01/.../06-...ipynb`](../../stages/01-ingestion/06-pdf-advanced-issues/06-pdf-advanced-issues.ipynb) | [`playground/01/.../02-...ipynb`](../../playground/01-ingestion/02-pdf-parsing.ipynb) | [x] مكتمل |
| 07 | **قراءة وتحليل مستندات وورد (Word DOCX)** | Lecture 14 | [الدليل الشامل](./STAGE_01_INGESTION_GUIDE.md#9-الدرس-07-قراءة-وتحليل-مستندات-word-07-word-documents) | [`stages/01/.../07-...ipynb`](../../stages/01-ingestion/07-word-documents/07-word-documents.ipynb) | [`playground/01/.../03-...ipynb`](../../playground/01-ingestion/03-word-parsing.ipynb) | [x] مكتمل |
| 08 | **معالجة ملفات الجداول CSV و Excel** | Lecture 15 | [الدليل الشامل](./STAGE_01_INGESTION_GUIDE.md#10-الدرس-08-استيعاب-البيانات-الجدولية-csv-و-excel-08-csv-excel) | [`stages/01/.../08-...ipynb`](../../stages/01-ingestion/08-csv-excel/08-csv-excel.ipynb) | [`playground/01/.../04-...ipynb`](../../playground/01-ingestion/04-csv-excel-parsing.ipynb) | [x] مكتمل |
| 09 | **قراءة وتحليل بيانات JSON شبه المهيكلة** | Lecture 16 | [الدليل الشامل](./STAGE_01_INGESTION_GUIDE.md#11-الدرس-09-معالجة-بيانات-json-شبه-المهيكلة-09-json-processing) | [`stages/01/.../09-...ipynb`](../../stages/01-ingestion/09-json-processing/09-json-processing.ipynb) | [`playground/01/.../05-...ipynb`](../../playground/01-ingestion/05-json-parsing.ipynb) | [x] مكتمل |
| 10 | **ربط واستخراج البيانات من قواعد بيانات SQL** | Lecture 17 | [الدليل الشامل](./STAGE_01_INGESTION_GUIDE.md#12-الدرس-10-ربط-واستخراج-قواعد-البيانات-العلائقية-10-sql-databases) | [`stages/01/.../10-...ipynb`](../../stages/01-ingestion/10-sql-databases/10-sql-databases.ipynb) | [`playground/01/.../06-...ipynb`](../../playground/01-ingestion/06-sql-parsing.ipynb) | [x] مكتمل |

---

## المعايير الهندسية للمرحلة
* **`stages/`**: كود إنتاجي مسبق التنفيذ بمخرجاته الكاملة، بتوثيق إنجليزي تقني صارم وخالٍ من الرموز التعبيرية مع فحوصات `Assertions`.
* **`playground/`**: كشكول تجارب تفاعلي ودود باللغة العربية البسيطة يتيح التجربة الحرة وتعديل المعاملات والمسارات دون قيود.
