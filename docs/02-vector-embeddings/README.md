# 02 - التضمينات الشعاعية (Vector Embeddings)

المرحلة الثانية في مسار إتقان الـ RAG، وتغطي **القسم السادس من الكورس (Section 6: Vector Embedding And Vector Databases - المحاضرات 19 إلى 23)**، وتركز على تحويل النصوص وقطع البيانات المجزأة (**Chunks**) إلى متجهات رقمية كثيفة (**Dense Vectors**) تعبر عن المعنى الدلالي في فضاء متعدد الأبعاد، وحساب التشابه الدلالي بينها عبر تقنيات مثل جيب التمام (Cosine Similarity).

---

## 🧭 خارطة موضوعات المرحلة (Curriculum)

| الرقم | المجلد الفرعي | عنوان الدرس (Topic) | الشرح (.md) | الدفتر المرجعي (.ipynb) | الحالة |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 01 | **[01-intro-to-embeddings](./01-intro-to-embeddings/)** | مقدمة في التضمينات وفكرة المتجهات (Intro to Embeddings & Vector Representations) | [README](./01-intro-to-embeddings/README.md) | [Notebook](./01-intro-to-embeddings/01-intro-to-embeddings.ipynb) | [x] مكتمل |
| 02 | **[02-visualization-cosine-similarity](./02-visualization-cosine-similarity/)** | التصور الرياضي والبصري للمتجهات وتشابه جيب التمام (Cosine Similarity Visuals) | [README](./02-visualization-cosine-similarity/README.md) | [Notebook](./02-visualization-cosine-similarity/02-visualization-cosine-similarity.ipynb) | [x] مكتمل |
| 03 | **[03-huggingface-embeddings](./03-huggingface-embeddings/)** | نماذج التضمين مفتوحة المصدر عبر HuggingFace Inference API | [README](./03-huggingface-embeddings/README.md) | [Notebook](./03-huggingface-embeddings/03-huggingface-embeddings.ipynb) | [x] مكتمل |
| 04 | **[04-openai-embeddings](./04-openai-embeddings/)** | تضمينات OpenAI والبحث الدلالي العملي (OpenAI Embeddings & Semantic Search) | [README](./04-openai-embeddings/README.md) | [Notebook](./04-openai-embeddings/04-openai-embeddings.ipynb) | [x] مكتمل |

---

## 🏛️ المعمارية العامة للمرحلة (Stage Architecture)

```mermaid
flowchart LR
    A["Text Chunks\n(From Stage 01)"] --> B["Embedding Model\n(HuggingFace / OpenAI)"]
    B --> C["Dense Vector\n([0.12, -0.45, ..., 0.89])"]
    C --> D["Mathematical Comparison\n(Cosine Similarity / Dot Product)"]
    D --> E["Semantic Search Results\n(Ranked by Relevance)"]
```
