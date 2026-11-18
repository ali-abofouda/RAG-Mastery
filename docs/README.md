# الدليل المعماري والمفاهيمي الشامل لمسار إتقان الـ RAG
### RAG Mastery Architecture & Engineering Handbook (`docs/`)

مرحباً بك في مجلد **التوثيق والشرح المعماري والمفاهيمي (`docs/`)**.

تم تصميم هذا المجلد ليكون **المرجع الهندسي الشامل والعملي** لأنظمة الـ RAG والوكلاء الأذكياء (Agentic AI). يعتمد التوثيق هنا على مبدأ **الشرح المرتكز على المعنى والمفاهيم (Concept-Driven Architecture)**؛ حيث يتم تفكيك كل مفهوم هندسي بعمق، توضيح دوافعه والبدائل المتاحة، ودعمه مباشرة **بكود بايثون تطبيقي كامل ومشروح**، بعيداً عن التعقيدات الرياضية النظرية المجردة.

---

## المبادئ الأربعة للتوثيق الهندسي الحديث (Core Documentation Pillars)

1. **التركيز على المعنى والهدف الهندسي (Concept-Driven Intuition)**:
   - تفكيك المشكلة الواقعية التي يعالجها كل مكون.
   - استبدال المعادلات الرياضية الجافة بمخططات تدفق تفاعلية (`Mermaid Diagrams`) وشروحات حدسية مباشرة.

2. **الكود التطبيقي الفعلي داخل التوثيق (Implementation in Action)**:
   - كل ملف توثيقي يحتوي على كود بايثون متكامل ونظيف وقابل للتشغيل الفوري.
   - تعليقات توضيحية احترافية (`Inline Comments`) توضح دور كل سطر وربطه بالمفهوم المعماري.

3. **المقارنات والمفاضلات الهندسية (Trade-offs & Decision Frameworks)**:
   - جداول مقارنة واضحة توضح متى نستخدم التقنية ومتى نفضل غيرها.
   - حساب التكاليف، أزمنة الاستجابة (`Latency`)، ومتطلبات الموارد.

4. **تحديات بيئات الإنتاج (Production Gotchas & Best Practices)**:
   - توثيق الأخطاء الشائعة وحالات الحافة (`Edge Cases`) والحلول المعتمدة في كبرى الشركات.

---

## خريطة الأدلة المعمارية للأقسام (Handbook Roadmap)

| القسم | المجلد | المفهوم الهندسي الشامل | الكود التطبيقي المدمج |
| :---: | :--- | :--- | :--- |
| **00** | [`00-rag-fundamentals/`](./00-rag-fundamentals/) | أسس معمارية الـ RAG، المقارنة مع Fine-Tuning، والمسار الكامل | Minimal End-to-End Working RAG Pipeline |
| **01** | [`01-ingestion/`](./01-ingestion/) | استخراج وتجهيز المستندات متعددة الصيغ بنمط Parse-Once | Multi-Format Document Ingestion & Parsers |
| **02** | [`02-vector-embeddings/`](./02-vector-embeddings/) | تمثيل المعاني دلالياً، فضاء المتجهات، ومقاييس المسافة عملياً | Dense Embeddings & Vector Similarity Engine |
| **03** | [`03-vector-stores-and-databases/`](./03-vector-stores-and-databases/) | قواعد بيانات المتجهات، آليات الفهرسة السريعة (HNSW)، والـ Payloads | Local & Cloud Vector DB Setup & Indexing |
| **04** | [`04-advanced-chunking/`](./04-advanced-chunking/) | استراتيجيات تقطيع النصوص وحفظ السياق والميتاداتا | Advanced Chunking Strategies Benchmark |
| **05** | [`05-hybrid-search-and-retrieval/`](./05-hybrid-search-and-retrieval/) | البحث الهجين (Dense + BM25) وخوارزميات إعادة الترتيب (RRF) | Production Hybrid Retriever & Cross-Encoder |
| **06** | [`06-query-enhancement/`](./06-query-enhancement/) | تحسين وصياغة الاستعلامات وتوليد الاستعلامات الفرعية و HyDE | Query Expansion & Rewriting Pipeline |
| **07** | [`07-multimodal-rag/`](./07-multimodal-rag/) | الـ RAG متعدد الوسائط واسترجاع الصور والرسوم البيانية | Dual-Stream Vision-Enhanced Multimodal Pipeline |
| **08** | [`08-agentic-ai-foundations/`](./08-agentic-ai-foundations/) | أسس وكلاء الذكاء الاصطناعي، الأركان الإدراكية، واستدعاء الأدوات | Tool-Using Autonomous Agent from Scratch |
| **09** | [`09-langchain-modern-updates/`](./09-langchain-modern-updates/) | بنية LangChain الحديثة وإدارة الحزم بالـ UV | Production LCEL Pipeline & Middleware |
| **10** | [`10-langgraph-fundamentals/`](./10-langgraph-fundamentals/) | معمارية Pregel/BSP، الرسوم البيانية الدائرية، والذاكرة المستمرة | Stateful Cyclic Graph Agent with Checkpointing |
| **30** | [`30-hr-policy-rag-assistant-with-ai-security/`](./30-hr-policy-rag-assistant-with-ai-security/) | المشروع المؤسسي المتكامل مع دروع أمان الذكاء الاصطناعي | Enterprise HR Assistant with Guardrails & Evals |
