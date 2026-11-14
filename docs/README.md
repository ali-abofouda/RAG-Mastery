# الدليل النظري والمعماري الشامل لمسار إتقان الـ RAG
### RAG Mastery Architecture & Theoretical Handbook (`docs/`)

مرحباً بك في مجلد **التوثيق والشرح النظري والمعماري (`docs/`)**.
هذا المجلد مخصص بالكامل لتقديم الفهم النظري العميق، المعمارية الهندسية، المعادلات الرياضية، ومخططات التدفق لكل درس في المسار، **دون أي كود تنفيذي مشتت**.

---

## 🧭 هيكلية مجلدات المشروع الثلاثة (The 3-Pillar Repository Architecture)

ينقسم المشروع إلى 3 مجلدات رئيسية واضحة ومستقلة:

1. **`docs/` (الشرح النظري والمعماري)**:
   - المفاهيم والأسس النظرية.
   - المخططات المعمارية (`Mermaid Diagrams`).
   - المعادلات والتحليلات الرياضية.
   - المقارنات والـ `Trade-offs` الهندسية.

2. **`stages/` (الكود النموذجي المرجعي)**:
   - الكود النموذجي الكامل والمنفذ مسبقاً (`Production-ready reference code`).
   - خلايا متسلسلة بتعليقات توضيحية احترافية (`Inline Comments`).
   - خالي تماماً من الإيموجي ومجهز بمخرجات التحقق الحقيقية.

3. **`playground/` (معمل التجارب والتطبيق العملي)**:
   - معمل التجارب المخصص للمتدرب لكتابة الكود بنفسه.
   - مساحات مخصصة للتجربة الحرة والتعديل العملي (`Hands-on Lab`).

---

## 📚 فهرس الشرح المعماري للمراحل

| المرحلة | المجلد الفرعي | موضوعات الشرح | الدليل التفصيلي |
| :---: | :--- | :--- | :---: |
| **00** | [`00-rag-fundamentals/`](./00-rag-fundamentals/) | مفاهيم وأساسيات أنظمة الـ RAG والفرق بين البحث التقليدي والدلالي | [README](./00-rag-fundamentals/README.md) |
| **01** | [`01-ingestion/`](./01-ingestion/) | معمارية استخراج وتفريغ المستندات بمختلف أنواعها | [README](./01-ingestion/README.md) |
| **02** | [`02-vector-embeddings/`](./02-vector-embeddings/) | نماذج التضمين، فضاء المتجهات، ومقاييس المسافة الدلالية | [README](./02-vector-embeddings/README.md) |
| **03** | [`03-vector-stores-and-databases/`](./03-vector-stores-and-databases/) | المعمارية الداخلية لقواعد وبيانات المتجهات المحلية والسحابية | [README](./03-vector-stores-and-databases/README.md) |
| **04** | [`04-advanced-chunking/`](./04-advanced-chunking/) | تقنيات التقطيع الدلالي المتقدم، قياس تشابه الجمل، ونقاط الانفصال | [README](./04-advanced-chunking/README.md) |
| **05** | [`05-hybrid-search-and-retrieval/`](./05-hybrid-search-and-retrieval/) | البحث الهجين، دمج المصفوفات، خوارزميات Reranking و MMR | [README](./05-hybrid-search-and-retrieval/README.md) |
| **06** | [`06-query-enhancement/`](./06-query-enhancement/) | تحسين وصياغة الاستعلامات وتوسيعها دلالياً (Query Expansion) | [README](./06-query-enhancement/README.md) |
| **07** | [`07-multimodal-rag/`](./07-multimodal-rag/) | الـ RAG متعدد الوسائط واسترجاع وفهرسة الصور والرسوم البيانية مع النصوص | [README](./07-multimodal-rag/README.md) |
| **08** | [`08-agentic-ai-foundations/`](./08-agentic-ai-foundations/) | أسس وكلاء الذكاء الاصطناعي، الأركان الإدراكية الأربعة، ومقارنة AI Agents ضد Agentic AI | [README](./08-agentic-ai-foundations/README.md) |
| **09** | [`09-langchain-modern-updates/`](./09-langchain-modern-updates/) | تحديثات LangChain v1+ الحديثة، مدير الحزم السريع UV، وبنية الـ Middleware | [README](./09-langchain-modern-updates/README.md) |
| **10** | [`10-langgraph-fundamentals/`](./10-langgraph-fundamentals/) | أساسيات LangGraph، معمارية Pregel/BSP، الرسوم البيانية الدائرية، والذاكرة المستمرة (HITL) | [README](./10-langgraph-fundamentals/README.md) |
| **15** | [`capstone/`](./capstone/) | المعمارية الشاملة لمشروع التطبيق النهائي المتكامل | [README](./capstone/README.md) |
