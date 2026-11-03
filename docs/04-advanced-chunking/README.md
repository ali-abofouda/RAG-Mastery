# المرحلة 04: تقنيات التقطيع الدلالي المتقدم
### Advanced Semantic Chunking Architecture (`docs/04-advanced-chunking/`)

تغطي هذه المرحلة بالكامل **القسم الثامن من الكورس (Section 8: Advanced Chunking And Preprocessing Techniques - المحاضرات 37 إلى 40)**.

تتناول هذه المرحلة الانتقال المعماري من التقطيع الحجمي الثابت القائم على عداد الحروف والرموز (`Fixed-Size Splitting`) إلى **التقطيع الدلالي الذكي (`Semantic Chunking`)** القائم على قياس اكتمال الأفكار واستمرار المعنى الرياضي بين الجمل.

---

## فهرس موضوعات المرحلة

| الرقم | عنوان الدرس النظري | المحاضرة المقابلة | الملف التوثيقي | الكود النموذجي (`stages/`) | معمل التجربة (`playground/`) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 01 | **أساسيات وخوارزمية التقطيع الدلالي ونقاط الانفصال** | Lecture 37 | [`01-semantic-chunking-fundamentals.md`](./01-semantic-chunking-fundamentals.md) | [`stages/04/.../01-...ipynb`](../../stages/04-advanced-chunking/01-semantic-chunking-fundamentals/01-semantic-chunking-fundamentals.ipynb) | [`playground/04/.../01-...ipynb`](../../playground/04-advanced-chunking/01-semantic-chunking-fundamentals.ipynb) |
| 02 | **بناء محرك التقطيع الدلالي بلغة بايثون من الصفر** | Lecture 38 | [`02-semantic-chunking-python.md`](./02-semantic-chunking-python.md) | [`stages/04/.../02-...ipynb`](../../stages/04-advanced-chunking/02-semantic-chunking-python/02-semantic-chunking-python.ipynb) | [`playground/04/.../02-...ipynb`](../../playground/04-advanced-chunking/02-semantic-chunking-python.ipynb) |
| 03 | **بناء مسار RAG كامل مدمج به كلاس التقطيع المعياري** | Lecture 39 | [`03-building-rag-semantic-chunker.md`](./03-building-rag-semantic-chunker.md) | [`stages/04/.../03-...ipynb`](../../stages/04-advanced-chunking/03-building-rag-semantic-chunker/03-building-rag-semantic-chunker.ipynb) | [`playground/04/.../03-...ipynb`](../../playground/04-advanced-chunking/03-building-rag-semantic-chunker.ipynb) |
| 04 | **التقطيع الدلالي الجاهز باستخدام مكتبة LangChain** | Lecture 40 | `04-semantic-chunking-langchain.md` | قيد العمل | قيد العمل |

---

## المعمارية العامة للتقطيع الدلالي (Semantic Chunking Architecture)

```mermaid
flowchart TD
    subgraph RawDoc ["1. المستند الخام"]
        Doc["Raw Multi-Topic Document\n(PDF / TXT / DOCX)"]
    end

    subgraph Phase1 ["2. التجزئة اللغوية (Segmentation)"]
        S1["الجملة S0: تعريف لانج تشين"]
        S2["الجملة S1: أدوات ومكتبات لانج تشين"]
        S3["الجملة S2: مكونات السلاسل والذاكرة"]
        S4["الجملة S3: برج إيفل في باريس"]
        S5["الجملة S4: السياحة في فرنسا"]
        Doc --> S1 & S2 & S3 & S4 & S5
    end

    subgraph Phase2 ["3. توليد المتجهات الكثيفة (Dense Embeddings)"]
        E0["Vector E0 (dim=384)"]
        E1["Vector E1 (dim=384)"]
        E2["Vector E2 (dim=384)"]
        E3["Vector E3 (dim=384)"]
        E4["Vector E4 (dim=384)"]
        S1 --> E0
        S2 --> E1
        S3 --> E2
        S4 --> E3
        S5 --> E4
    end

    subgraph Phase3 ["4. قياس تشابه الجمل المتجاورة (Pairwise Cosine Similarity)"]
        Sim01["Sim(E0, E1) = 0.8248\n(ترابط دلالي عالي جداً)"]
        Sim12["Sim(E1, E2) = 0.4487\n(ترابط متوسط)"]
        Sim23["Sim(E2, E3) = 0.0225\n[انهيار دلالي حاد Cliff Drop!]"]
        Sim34["Sim(E3, E4) = 0.3776\n(ترابط متوسط)"]
        E0 & E1 --> Sim01
        E1 & E2 --> Sim12
        E2 & E3 --> Sim23
        E3 & E4 --> Sim34
    end

    subgraph Phase4 ["5. التجميع بالعتبة وفصل القطع (Breakpoint Detection)"]
        Cond{"هل Sim >= Threshold؟"}
        Sim01 & Sim12 & Sim23 & Sim34 --> Cond
        ChunkA["القطعة 1: سياق نقي عن لانج تشين والذكاء الاصطناعي"]
        ChunkB["القطعة 2: سياق نقي عن معالم وسياحة فرنسا"]
        Cond -->|نعم: دمج| ChunkA
        Cond -->|لا: نقطة انفصال Breakpoint| ChunkB
        Cond -->|نعم: دمج| ChunkB
    end

    subgraph Phase5 ["6. التخزين والاسترجاع (FAISS & LCEL)"]
        ChunkA & ChunkB --> VDB["قاعدة متجهات FAISS"]
        VDB --> Retriever["Retriever (k=2)"]
        Retriever --> LLM["ChatGroq Inference"]
    end
```

---

## المقارنة الهندسية: التقطيع الحجمي مقابل التقطيع الدلالي

| معيار المقارنة | التقطيع الحجمي الثابت (`RecursiveCharacterTextSplitter`) | التقطيع الدلالي المتقدم (`Semantic Chunking`) |
| :--- | :--- | :--- |
| **أساس التقطيع** | عدد الحروف أو التوكنز الثابت (مثلاً 500 حرف) | درجة الترابط الدلالي وانتقال موضوع الفكرة |
| **سلامة السياق** | منخفضة جداً؛ قد يتم قطع الفكرة في منتصفها | ممتازة؛ كل قطعة تحتوي على فكرة مكتملة ومستقلة |
| **نقاء المتجهات (Signal-to-Noise)** | مشوش؛ يدمج موضوعات مختلفة في نفس المتجه | نقي 100%؛ المتجه يمثل معنى واحداً واضحاً ومحدداً |
| **التكلفة والسرعة في الـ Ingestion** | فوري وبدون أي تكلفة حسابية ($O(N)$) | يتطلب حساب متجهات التضمين للجمل أولاً |
| **أثر الإنتاج على الـ RAG** | احتمالية هلوسة واسترجاع سياق مشتت وغير متصل | استرجاع فائق الدقة وانعدام الهلوسة الناتجة عن تشتت السياق |
