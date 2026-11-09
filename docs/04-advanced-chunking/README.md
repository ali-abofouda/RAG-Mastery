# المرحلة 04: التقطيع الدلالي المتقدم (Advanced Semantic Chunking)
### Comprehensive Architectural Guide (`docs/04-advanced-chunking/`)

المرحلة الرابعة في مسار إتقان الـ RAG، وتغطي تقنيات التقطيع الذكي المبني على دلالة المعنى واكتمال الفكرة، والتخلص النهائي من عيوب التقطيع الحجمي الثابت عبر خوارزميات نقاط الانفصال الدلالي (`Semantic Breakpoints`) والعتبات الإحصائية.

---

## الدليل المعماري الموحد للمرحلة (Master Guide)

📄 **[الدليل الشامل للتقطيع الدلالي المتقدم (01-semantic-chunking-master-guide.md)](./01-semantic-chunking-master-guide.md)**
* **المحاضرات المشمولة**: المحاضرات 37، 38، 39، 40 (القسم الثامن كامل).
* **المحتوى العلمي الموحد**:
  * قصور التقطيع الحجمي التقليدي (تمزيق السياق وتلوث المتجهات).
  * خوارزمية التقطيع الدلالي خطوة بخطوة والتنعيم السياقي (`Buffer Window Smoothing`).
  * الرياضيات الصارمة للعتبات الإحصائية الأربعة (`Percentile`, `Standard Deviation`, `IQR`, `Gradient Drops`).
  * تحليل منحنيات هبوط التشابه الحاد (`Similarity Cliff Drop`).
  * التطبيق الإنتاجي عبر أداة `SemanticChunker` في LangChain.
  * مصفوفة المفاضلة الهندسية الشاملة وأسئلة المقابلات المتقدمة للـ Senior AI Engineers.

---

## فهرس المشاريع البرمجية التابعة للمرحلة

| الرقم | عنوان المشروع البرمجي | المحاضرة المقابلة | الكود المرجعي (`stages/`) | معمل التجربة (`playground/`) | الحالة |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 01 | **أساسيات وخوارزمية التقطيع الدلالي من الصفر** | Lecture 37 | [`01-...ipynb`](../../stages/04-advanced-chunking/01-semantic-chunking-fundamentals/01-semantic-chunking-fundamentals.ipynb) | [`01-...ipynb`](../../playground/04-advanced-chunking/01-semantic-chunking-fundamentals.ipynb) | مكتمل |
| 02 | **التنفيذ البرمجي للخوارزمية ورسم المنحنيات** | Lecture 38 | [`02-...ipynb`](../../stages/04-advanced-chunking/02-semantic-chunking-python/02-semantic-chunking-python.ipynb) | [`02-...ipynb`](../../playground/04-advanced-chunking/02-semantic-chunking-python.ipynb) | مكتمل |
| 03 | **دمج التقطيع الدلالي في مسار RAG متكامل** | Lecture 39 | [`03-...ipynb`](../../stages/04-advanced-chunking/03-building-rag-semantic-chunker/03-building-rag-semantic-chunker.ipynb) | [`03-...ipynb`](../../playground/04-advanced-chunking/03-building-rag-semantic-chunker.ipynb) | مكتمل |
| 04 | **تطبيق SemanticChunker المدمج في LangChain** | Lecture 40 | [`04-...ipynb`](../../stages/04-advanced-chunking/04-semantic-chunking-langchain/04-semantic-chunking-langchain.ipynb) | [`04-...ipynb`](../../playground/04-advanced-chunking/04-semantic-chunking-langchain.ipynb) | مكتمل |

---

## المعايير الهندسية للمرحلة
* **`stages/`**: كود إنتاجي Senior مسبق التنفيذ بمخرجاته الكاملة، بتوثيق إنجليزي فني صارم وخالٍ من الرموز التعبيرية مع فحوصات `Assertions`.
* **`playground/`**: كشكول تجارب تفاعلي ودود باللغة العربية البسيطة يتيح التجربة الحرة وتعديل المعاملات والمسارات دون قيود.
* **`docs/`**: دليل معماري موحد وفائق الدقة يجمع النظرية والرياضيات والأنظمة في مرجع شامل متماسك.
