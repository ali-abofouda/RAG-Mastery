# قاموس ومعجم مصطلحات هندسة الذكاء الاصطناعي (AI Engineering Glossary)

> **الهدف:** مرجع هندسي شامل ومبسط يشرح أهم وأدق المصطلحات التقنية في مجال هندسة الذكاء الاصطناعي (AI Engineering)، وأنظمة الـ RAG، والوكلاء الذكيين (Agents)، وتقييم النماذج، والبنية التحتية الإنتاجية.
> **المنهجية:** شرح مبني على **المفهوم العملي (Intuition-First)**، بدون حشو أكاديمي، مع توضيح: *لماذا تم ابتكار المصطلح؟ وما المشكلة التي يحلها في بيئة الإنتاج؟*

---

## 🗂️ التصنيف الهيكلي للملفات (Topic-Based Categorization)

| الملف | المجال التقني | أهم المصطلحات المغطاة |
| :--- | :--- | :--- |
| **[01-rag-and-retrieval.md](./01-rag-and-retrieval.md)** | **أنظمة RAG والاسترجاع** | `Dense vs Sparse`, `Hybrid Search`, `BM25`, `Cross-Encoder Reranker`, `Semantic Chunking`, `Parent-Document Retrieval`, `Reciprocal Rank Fusion (RRF)`, `Lost in the Middle`. |
| **[02-llm-foundations-and-inference.md](./02-llm-foundations-and-inference.md)** | **النماذج التوليدية والاستدلال** | `Context Window`, `Tokenization`, `Self-Attention`, `KV Cache`, `Quantization (AWQ/GPTQ)`, `vLLM`, `Speculative Decoding`, `Temperature`, `Top-p`. |
| **[03-agentic-ai-and-workflows.md](./03-agentic-ai-and-workflows.md)** | **الوكلاء وسير العمل (Agents)** | `LangGraph StateGraph`, `Tool Calling`, `ReAct Architecture`, `Routers & Conditional Edges`, `Model Context Protocol (MCP)`, `Human-in-the-Loop`, `Checkpointers`. |
| **[04-evaluation-and-observability.md](./04-evaluation-and-observability.md)** | **التقييم والمراقبة (Evals)** | `Ragas`, `Faithfulness`, `Answer Relevance`, `Context Precision/Recall`, `LLM-as-a-Judge`, `Tracing (LangSmith)`, `Guardrails`, `Prompt Injection`, `Red Teaming`. |
| **[05-training-and-adaptation.md](./05-training-and-adaptation.md)** | **التدريب والموائمة** | `Fine-Tuning`, `PEFT`, `LoRA & QLoRA`, `DPO (Direct Preference Optimization)`, `RLHF`, `Catastrophic Forgetting`, `Synthetic Data`. |
| **[06-data-and-infrastructure.md](./06-data-and-infrastructure.md)** | **البيانات والبنية التحتية** | `Vector Databases`, `HNSW Index`, `Cosine Similarity vs Dot Product`, `Semantic Caching`, `LLM Gateways`, `Docker Containerization`, `Streaming (SSE)`. |

---

## 🔍 الفهرس الأبجدي السريع (Quick Alphabetical Index)

| المصطلح بالإنجليزية | الترجمة / المفهوم | الملف المرجعي |
| :--- | :--- | :--- |
| **Agentic RAG** | الـ RAG المعتمد على وكيل ذكي يتخذ قرارات الاسترجاع ذاتياً | `03-agentic-ai-and-workflows.md` |
| **BM25** | خوارزمية بحث كلاسيكية مطورة بالكلمات المفتاحية (Sparse) | `01-rag-and-retrieval.md` |
| **Checkpointer** | آلية حفظ حالة وسياق المحادثة في قاعدة بيانات دائمة | `03-agentic-ai-and-workflows.md` |
| **Context Window** | نافذة السياق (الحد الأقصى للتوكنز التي يستوعبها النموذج) | `02-llm-foundations-and-inference.md` |
| **Corrective RAG (CRAG)** | تقييم وتصحيح المستندات المسترجعة قبل توليد الإجابة | `01-rag-and-retrieval.md` |
| **Cross-Encoder** | نموذج إعادة ترتيب دقيق يقارن السؤال بالمستند معاً | `01-rag-and-retrieval.md` |
| **Dense Embeddings** | متجهات دلالية رقمية كثيفة تلتقط المعنى والسياق | `01-rag-and-retrieval.md` |
| **DPO** | موائمة النماذج مباشرة مع تفضيلات المستخدم بدون نموذج مكافأة | `05-training-and-adaptation.md` |
| **Faithfulness** | مقياس إثبات أن الإجابة خالية من الهلوسة ومبنية على السياق | `04-evaluation-and-observability.md` |
| **Fine-Tuning** | إعادة تدريب أوزان النموذج على بيانات تخصصية | `05-training-and-adaptation.md` |
| **Guardrails** | دروع أمان تتحقق من سلامة المدخلات والمخرجات ومنع الاختراق | `04-evaluation-and-observability.md` |
| **HNSW** | أسرع فهرس للبحث التقريبي عن أقرب الجيران في الفيكتورز | `06-data-and-infrastructure.md` |
| **Hybrid Search** | دمج البحث الدلالي (Dense) مع البحث بالكلمات المفتاحية (Sparse) | `01-rag-and-retrieval.md` |
| **KV Cache** | ذاكرة كاش تحفظ المفاتيح والقيم لتسريع توليد التوكنز في الـ LLM | `02-llm-foundations-and-inference.md` |
| **LLM-as-a-Judge** | استخدام نموذج لغوي قوي ومحايد لتقييم مخرجات نظام آخر | `04-evaluation-and-observability.md` |
| **LoRA / QLoRA** | تدريب مصفوفات منخفضة الرتبة لتقليل استهلاك كروت الشاشة | `05-training-and-adaptation.md` |
| **Model Context Protocol (MCP)** | بروتوكول موحد لربط النماذج بالأدوات وقواعد البيانات الخارجية | `03-agentic-ai-and-workflows.md` |
| **Quantization** | ضغط أوزان النموذج (مثلاً من 16-bit إلى 4-bit) لتوفير الذاكرة | `02-llm-foundations-and-inference.md` |
| **Ragas** | إطار العمل القياسي عالمياً لتقييم أنظمة الـ RAG رقمياً | `04-evaluation-and-observability.md` |
| **ReAct Architecture** | نمط استدلال وتنفيذ يجمع بين التفكير (Reasoning) والفعل (Action) | `03-agentic-ai-and-workflows.md` |
| **Reciprocal Rank Fusion (RRF)** | خوارزمية رياضية لدمج وترتيب نتائج البحث من عدة مصادر | `01-rag-and-retrieval.md` |
| **Semantic Caching** | حفظ إجابات الأسئلة المتشابهة دلالياً لتوفير الوقت والتكلفة | `06-data-and-infrastructure.md` |
| **Semantic Chunking** | تقطيع النصوص بناءً على اكتمال المعنى وتغير الموضوع | `01-rag-and-retrieval.md` |
| **vLLM** | محرك فائق السرعة لاستضافة وتشغيل النماذج في بيئة الإنتاج | `02-llm-foundations-and-inference.md` |
