# 04 - تقنيات التقطيع الدلالي المتقدم (Advanced Semantic Chunking)

المرحلة الرابعة في مسار إتقان الـ RAG، وتغطي بالكامل **القسم الثامن من الكورس (Section 8: Advanced Chunking And Preprocessing Techniques - المحاضرات 37 إلى 40)**.

تتناول هذه المرحلة الانتقال من التقطيع البسيط القائم على حساب عدد الأحرف والرموز (`Fixed-Size Character Splitting`) إلى **التقطيع الدلالي الذكي (`Semantic Chunking`)** القائم على قياس المعنى والترابط الموضوعي بين الجمل.

---

## 🧭 خارطة موضوعات المرحلة (Curriculum)

| الرقم | المجلد الفرعي | عنوان الدرس (Topic) | المحاضرة المقابلة | الشرح (.md) | الدفتر المرجعي (.ipynb) | الحالة |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| 01 | **[01-semantic-chunking-fundamentals](./01-semantic-chunking-fundamentals/)** | أساسيات وخوارزمية التقطيع الدلالي ونقاط الانفصال | Lecture 37 | [README](./01-semantic-chunking-fundamentals/README.md) | [Notebook](./01-semantic-chunking-fundamentals/01-semantic-chunking-fundamentals.ipynb) | [x] مكتمل |
| 02 | **[02-semantic-chunking-python](./02-semantic-chunking-python/)** | بناء محرك التقطيع الدلالي بلغة بايثون من الصفر | Lecture 38 | [README](./02-semantic-chunking-python/README.md) | [Notebook](./02-semantic-chunking-python/02-semantic-chunking-python.ipynb) | [x] مكتمل |
| 03 | **[03-building-rag-semantic-chunker](./03-building-rag-semantic-chunker/)** | بناء مسار RAG كامل مدمج به الـ Semantic Chunker | Lecture 39 | [README](./03-building-rag-semantic-chunker/README.md) | [Notebook](./03-building-rag-semantic-chunker/03-building-rag-semantic-chunker.ipynb) | [x] مكتمل |
| 04 | **04-semantic-chunking-langchain** | التقطيع الدلالي الجاهز باستخدام مكتبة LangChain | Lecture 40 | قيد العمل | قيد العمل | [ ] قادم |

---

## 🏛️ المعمارية العامة للتقطيع الدلالي (Semantic Chunking Architecture)

```mermaid
flowchart TD
    subgraph RawDoc ["المستند الخام"]
        Doc["Raw Text Document\n(PDF / TXT / DOCX)"]
    end

    subgraph Phase1 ["المرحلة 1: تجزئة الجمل (Segmentation)"]
        S1["الجملة 1: فكرة عن لانج تشين"]
        S2["الجملة 2: فكرة تابعة عن لانج تشين"]
        S3["الجملة 3: فكرة مفاجئة عن باريس"]
        S4["الجملة 4: فكرة تابعة عن باريس"]
        Doc --> S1 & S2 & S3 & S4
    end

    subgraph Phase2 ["المرحلة 2: متجهات التضمين (Embeddings)"]
        E1["Vector E1 (dim=384)"]
        E2["Vector E2 (dim=384)"]
        E3["Vector E3 (dim=384)"]
        E4["Vector E4 (dim=384)"]
        S1 --> E1
        S2 --> E2
        S3 --> E3
        S4 --> E4
    end

    subgraph Phase3 ["المرحلة 3: قياس تشابه الجمل المتجاورة"]
        Sim12["Sim(E1, E2) = 0.55\n(تشابه عالي -> نفس الموضوع)"]
        Sim23["Sim(E2, E3) = 0.08\n(هبوط حاد -> تغير الموضوع!)"]
        Sim34["Sim(E3, E4) = 0.77\n(تشابه عالي -> نفس الموضوع)"]
        E1 & E2 --> Sim12
        E2 & E3 --> Sim23
        E3 & E4 --> Sim34
    end

    subgraph Phase4 ["المرحلة 4: الدمج والفصل عند العتبة (Threshold)"]
        Threshold{"هل التشابه >= Threshold؟"}
        ChunkA["القطعة الدلالية الأولى [Chunk 1]:\nالجملة 1 + الجملة 2 (سياق نقي عن لانج تشين)"]
        ChunkB["القطعة الدلالية الثانية [Chunk 2]:\nالجملة 3 + الجملة 4 (سياق نقي عن باريس)"]
        Sim12 -->|نعم: دمج| ChunkA
        Sim23 -->|لا: نقطة انفصال Breakpoint| ChunkB
        Sim34 -->|نعم: دمج| ChunkB
    end

    subgraph Storage ["التخزين والاسترجاع"]
        ChunkA & ChunkB --> VDB["قاعدة بيانات المتجهات\n(Pinecone / AstraDB / ChromaDB)"]
    end
```

---

## ⚖️ المقارنة: التقطيع العادي مقابل التقطيع الدلالي

| وجه المقارنة | التقطيع العادي (`RecursiveCharacterTextSplitter`) | التقطيع الدلالي (`Semantic Chunking`) |
| :--- | :--- | :--- |
| **معيار التقطيع** | عدد الحروف والرموز الثابتة (مثلاً 500 حرف) | التشابه الدلالي وتغير سياق الفكرة |
| **سلامة الجمل والأفكار** | منخفضة (قد يتم قطع الجملة في منتصفها) | ممتازة (كل قطعة تمثل فكرة كاملة ومستقلة) |
| **نقاء المتجهات (Vector Purity)** | مشوش؛ يخلط موضوعات مختلفة في نفس القطعة | نقي 100%؛ المتجه يمثل معنى واحداً واضحاً |
| **التكلفة والسرعة** | فائقة السرعة وفورية (مجرد تقطيع نصوص) | تتطلب حساب Embeddings لكل جملة أولاً |
| **التأثير على الـ RAG** | زيادة خطر الهلوسة وضعف دقة الاسترجاع | استرجاع دقيق وإجابات موثقة بالكامل من السياق |
