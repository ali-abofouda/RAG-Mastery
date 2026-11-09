# 07 - الـ RAG متعدد الوسائط (Multimodal RAG)
### Comprehensive Architectural Guide (`docs/07-multimodal-rag/`)

المرحلة السابعة في مسار إتقان الـ RAG، وتركز على الانتقال الحاسم من التعامل مع النصوص الأحادية (`Unimodal Text`) إلى استيعاب وفهرسة واسترجاع الوثائق الغنية متعددة الوسائط (`Multimodal Documents: Text + Images`)، كالتقارير المالية والرسوم البيانية والمخططات الهندسية المعمارية.

---

## الدليل المعماري الموحد للمرحلة (Master Guide)

📄 **[الدليل الشامل للـ RAG متعدد الوسائط لملفات الـ PDF والصور (01-multimodal-rag-master-guide.md)](./01-multimodal-rag-master-guide.md)**
* **المحاضرات المشمولة**: المحاضرتان 53 و 54 (Stage 07).
* **المحتوى العلمي الموحد**:
  * الفجوة المعمارية بين الـ Unimodal والـ Multimodal RAG وتجاوز فخ تجاهل المخططات البيانية.
  * النماذج اللغوية البصرية (`VLMs`) وآلية معالجة الرموز البصرية (`Vision Patches/Tokens`).
  * فضاء التضمين الموحد والرياضيات الحاكمة لنموذج `CLIP` وخسارة التدريب التقابلي (`InfoNCE Loss`).
  * خط المعالجة البرمجي المتكامل: استخراج متوازي للنصوص والصور عبر `PyMuPDF (fitz)`.
  * المعالجة والتضمين المشترك وتشفير الصور بصيغة `Base64` في الميتا-داتا.
  * الفهرسة والبحث الهجين عابر الوسائط عبر `FAISS FlatIP`.
  * صياغة رسائل النماذج البصرية (`Multimodal Message Formatting`) للاستدلال والتحليل.
  * مصفوفة المفاضلة الهندسية في تخزين الصور وأسئلة المقابلات المتقدمة للـ Senior AI Engineers.

---

## فهرس المشاريع البرمجية التابعة للمرحلة

| الرقم | عنوان الموضوع البرمجي | المحاضرة المقابلة | الكود المرجعي (`stages/`) | معمل التجربة (`playground/`) | الحالة |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 01 | **معمارية وأسس الـ Multimodal RAG ونموذج CLIP** | Lecture 53 | [`01-multimodal-architecture.ipynb`](../../stages/07-multimodal-rag/01-multimodal-architecture/01-multimodal-architecture.ipynb) | [`01-multimodal-architecture.ipynb`](../../playground/07-multimodal-rag/01-multimodal-architecture.ipynb) | مكتمل |
| 02 | **التطبيق العملي للـ Multimodal RAG لملفات PDF والصور** | Lecture 54 | [`02-multimodal-pdf-implementation.ipynb`](../../stages/07-multimodal-rag/02-multimodal-pdf-implementation/02-multimodal-pdf-implementation.ipynb) | [`02-multimodal-pdf-implementation.ipynb`](../../playground/07-multimodal-rag/02-multimodal-pdf-implementation.ipynb) | مكتمل |

---

## المعايير الهندسية للمرحلة
* **`stages/`**: كود إنتاجي Senior مسبق التنفيذ بمخرجاته الكاملة، بتوثيق إنجليزي فني صارم وخالٍ من الرموز التعبيرية مع فحوصات `Assertions`.
* **`playground/`**: كشكول تجارب تفاعلي ودود باللغة العربية البسيطة يتيح التجربة الحرة وتعديل المعاملات والمسارات دون قيود.
* **`docs/`**: دليل معماري موحد وفائق الدقة يجمع النظرية والرياضيات والأنظمة في مرجع شامل متماسك.
