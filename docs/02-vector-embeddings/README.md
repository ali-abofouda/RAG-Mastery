# المرحلة 02: التضمينات وفضاء المتجهات (Vector Embeddings)
### Comprehensive Architectural Guide (`docs/02-vector-embeddings/`)

المرحلة الثانية في مسار إتقان الـ RAG، وتهتم بتحويل النصوص والوثائق إلى متجهات عددية كثيفة (`Dense Vectors`) في فضاء رياضي متعدد الأبعاد، بحيث تعبر الزاوية والمسافة بين المتجهات عن درجة التشابه الدلالي في المعنى الحقيقي.

---

## فهرس موضوعات ومشاريع المرحلة

| الرقم | عنوان الموضوع البرمجي | الشرح المعماري (`docs/`) | الكود المرجعي (`stages/`) | معمل التجربة (`playground/`) | الحالة |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 01 | **مقدمة في التضمينات وفضاء المتجهات والهندسة الخطية** | [01-intro-to-embeddings.md](./01-intro-to-embeddings.md) | [`01-intro-to-embeddings.ipynb`](../../stages/02-vector-embeddings/01-intro-to-embeddings/01-intro-to-embeddings.ipynb) | [`01-intro-to-embeddings.ipynb`](../../playground/02-vector-embeddings/01-intro-to-embeddings.ipynb) | مكتمل |
| 02 | **مقاييس المسافة والتشابه الرياضي ومبرهنة التطبيع L2** | [02-distance-metrics-and-similarity.md](./02-distance-metrics-and-similarity.md) | [`02-visualization-cosine-similarity.ipynb`](../../stages/02-vector-embeddings/02-visualization-cosine-similarity/02-visualization-cosine-similarity.ipynb) | [`02-visualization-and-similarity.ipynb`](../../playground/02-vector-embeddings/02-visualization-and-similarity.ipynb) | مكتمل |
| 03 | **نماذج التضمين المحلية مفتوحة المصدر عبر HuggingFace** | [03-huggingface-local-embeddings.md](./03-huggingface-local-embeddings.md) | [`03-huggingface-embeddings.ipynb`](../../stages/02-vector-embeddings/03-huggingface-embeddings/03-huggingface-embeddings.ipynb) | [`03-huggingface-embeddings.ipynb`](../../playground/02-vector-embeddings/03-huggingface-embeddings.ipynb) | مكتمل |
| 04 | **نماذج التضمين التجارية وتقنية ماتريوشكا MRL** | [04-openai-and-commercial-embeddings.md](./04-openai-and-commercial-embeddings.md) | [`04-openai-embeddings.ipynb`](../../stages/02-vector-embeddings/04-openai-embeddings/04-openai-embeddings.ipynb) | [`04-openai-and-semantic-search.ipynb`](../../playground/02-vector-embeddings/04-openai-and-semantic-search.ipynb) | مكتمل |

---

## المعايير الهندسية للمرحلة
* **`stages/`**: كود إنتاجي Senior مسبق التنفيذ بمخرجاته الكاملة، بتوثيق إنجليزي فني صارم وخالٍ من الرموز التعبيرية مع فحوصات `Assertions`.
* **`playground/`**: كشكول تجارب تفاعلي ودود باللغة العربية البسيطة يتيح التجربة الحرة وتعديل المعاملات والمسارات دون قيود.
* **`docs/`**: مذكرات معمارية وتفصيلية متخصصة ومصاغة وفق أعلى معايير هندسة النظم، متضمنة مخططات Mermaid، صياغات رياضية، ومصفوفات مفاضلة، وأسئلة مقابلات تقنية متقدمة.
