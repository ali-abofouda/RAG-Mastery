# المرحلة 01: معالجة واستيعاب البيانات (Data Ingestion & Parsing)
### Comprehensive Architectural Guide (`docs/01-ingestion/`)

المرحلة الأولى في رحلة التطبيق العملي لأنظمة الـ RAG، وتركز على كيفية استيراد وتحليل وتجزئة مختلف أنواع ومصادر البيانات لتحويلها إلى صيغة قابلة للتضمين والبحث الدلالي.

---

## فهرس موضوعات ومشاريع المرحلة

| الرقم | عنوان الموضوع البرمجي | الشرح المعماري (`docs/`) | الكود المرجعي (`stages/`) | معمل التجربة (`playground/`) | الحالة |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 01 | **إعداد بيئة العمل وهيكل المشروع باستخدام UV** | [01-environment-setup.md](./01-environment-setup.md) | [`01-environment-setup.ipynb`](../../stages/01-ingestion/01-environment-setup/01-environment-setup.ipynb) | [`01-text-parsing.ipynb`](../../playground/01-ingestion/01-text-parsing.ipynb) | مكتمل |
| 02 | **بنية كائن الـ Document وهندسة البيانات الوصفية** | [02-document-structure.md](./02-document-structure.md) | [`02-document-structure.ipynb`](../../stages/01-ingestion/02-document-structure/02-document-structure.ipynb) | [`01-text-parsing.ipynb`](../../playground/01-ingestion/01-text-parsing.ipynb) | مكتمل |
| 03 | **قراءة واستيراد الملفات النصية TextLoader والترميز** | [03-text-loaders.md](./03-text-loaders.md) | [`03-text-loaders.ipynb`](../../stages/01-ingestion/03-text-loaders/03-text-loaders.ipynb) | [`01-text-parsing.ipynb`](../../playground/01-ingestion/01-text-parsing.ipynb) | مكتمل |
| 04 | **استراتيجيات وتقنيات تجزئة النصوص Text Splitting** | [04-text-splitting.md](./04-text-splitting.md) | [`04-text-splitting.ipynb`](../../stages/01-ingestion/04-text-splitting/04-text-splitting.ipynb) | [`01-text-parsing.ipynb`](../../playground/01-ingestion/01-text-parsing.ipynb) | مكتمل |
| 05 | **قراءة واستخراج مستندات PDF ومقارنة المحملات** | [05-pdf-parsing.md](./05-pdf-parsing.md) | [`05-pdf-parsing.ipynb`](../../stages/01-ingestion/05-pdf-parsing/05-pdf-parsing.ipynb) | [`02-pdf-parsing.ipynb`](../../playground/01-ingestion/02-pdf-parsing.ipynb) | مكتمل |
| 06 | **حل المشكلات المعقدة في الـ PDF والخط الإنتاجي** | [06-pdf-advanced-issues.md](./06-pdf-advanced-issues.md) | [`06-pdf-advanced-issues.ipynb`](../../stages/01-ingestion/06-pdf-advanced-issues/06-pdf-advanced-issues.ipynb) | [`02-pdf-parsing.ipynb`](../../playground/01-ingestion/02-pdf-parsing.ipynb) | مكتمل |
| 07 | **قراءة وتحليل مستندات وورد (Word DOCX)** | [07-word-documents.md](./07-word-documents.md) | [`07-word-documents.ipynb`](../../stages/01-ingestion/07-word-documents/07-word-documents.ipynb) | [`03-word-parsing.ipynb`](../../playground/01-ingestion/03-word-parsing.ipynb) | مكتمل |
| 08 | **معالجة ملفات الجداول CSV و Excel والسرد الدلالي** | [08-csv-excel.md](./08-csv-excel.md) | [`08-csv-excel.ipynb`](../../stages/01-ingestion/08-csv-excel/08-csv-excel.ipynb) | [`04-csv-excel-parsing.ipynb`](../../playground/01-ingestion/04-csv-excel-parsing.ipynb) | مكتمل |
| 09 | **معالجة بيانات JSON شبه المهيكلة واستعلامات jq** | [09-json-processing.md](./09-json-processing.md) | [`09-json-processing.ipynb`](../../stages/01-ingestion/09-json-processing/09-json-processing.ipynb) | [`05-json-parsing.ipynb`](../../playground/01-ingestion/05-json-parsing.ipynb) | مكتمل |
| 10 | **ربط واستخراج البيانات من قواعد بيانات SQL** | [10-sql-databases.md](./10-sql-databases.md) | [`10-sql-databases.ipynb`](../../stages/01-ingestion/10-sql-databases/10-sql-databases.ipynb) | [`06-sql-parsing.ipynb`](../../playground/01-ingestion/06-sql-parsing.ipynb) | مكتمل |

---

## المعايير الهندسية للمرحلة
* **`stages/`**: كود إنتاجي مسبق التنفيذ بمخرجاته الكاملة، بتوثيق إنجليزي تقني صارم وخالٍ من الرموز التعبيرية مع فحوصات `Assertions`.
* **`playground/`**: كشكول تجارب تفاعلي ودود باللغة العربية البسيطة يتيح التجربة الحرة وتعديل المعاملات والمسارات دون قيود.
* **`docs/`**: مذكرات معمارية وتفصيلية متخصصة ومصاغة وفق أعلى معايير هندسة النظم، متضمنة مخططات Mermaid، صياغات رياضية، ومصفوفات مفاضلة، وأسئلة مقابلات تقنية متقدمة.
