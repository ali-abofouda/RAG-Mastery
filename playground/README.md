# المختبر العام الموحد لمشروع RAG Mastery (Project Playground)

مرحبًا بك في **المختبر العام الموحد (Unified Playground)** لمشروع RAG Mastery.  
تم تجميع ونقل كافة مساحات التجارب الحرة (Playgrounds) من داخل مجلدات المراحل الفرعية إلى هذا المجلد الرئيسي الخارجي المنظم حسب الأقسام والمراحل، بالإضافة إلى نوتبوك عام يربط دورة حياة الـ RAG كاملة.

---

## 📂 الهيكل التنظيمي للمختبر (Directory Structure)

```
playground/
│
├── playground.ipynb                             # المختبر العام الشامل للمشروع ككل (End-to-End)
├── IMPORTS_REFERENCE.md                         # الدليل الشامل لجميع الاستيرادات الحديثة وشرحها
├── README.md                                    # دليل المختبرات وطريقة الاستخدام
│
├── 01-ingestion/                                # تجارب المرحلة الأولى: استيراد وتفريغ المستندات
│   ├── 01-text-parsing.ipynb                    # تفريغ وقراءة الملفات النصية الخام (.txt)
│   ├── 02-pdf-parsing.ipynb                     # معالجة وتفريغ ملفات الـ PDF
│   ├── 03-word-parsing.ipynb                    # استخراج النصوص من ملفات Word (.docx)
│   ├── 04-csv-excel-parsing.ipynb               # قراءة ومعالجة البيانات الجدولية (CSV / Excel)
│   ├── 05-json-parsing.ipynb                    # معالجة وتحليل ملفات JSON وهياكلها
│   └── 06-sql-parsing.ipynb                     # الاتصال بقواعد البيانات واستخراج السجلات
│
├── 02-vector-embeddings/                        # تجارب المرحلة الثانية: التضمينات والتشابه الدلالي
│   ├── 01-indexing.ipynb                        # تجارب التضمين السحابي
│   ├── 02-huggingface-embedding.ipynb           # تجارب نماذج HuggingFace
│   ├── 3-openai-embedding.ipynb                 # تجارب نماذج OpenAI
│   └── 4-similarity-search.ipynb                # البحث الدلالي ومصفوفات التشابه
│
└── 03-vector-stores-and-databases/              # تجارب المرحلة الثالثة: فهارس وقواعد بيانات المتجهات
    └── 01-vector-stores-vs-vector-databases.ipynb # المقارنة العملية وسرعة الاسترجاع
```

---

## 🎯 أقسام المختبر (Playground Sections)

### 1. المختبر العام للمشروع ككل ([`playground.ipynb`](playground.ipynb))
المختبر التفاعلي الشامل الذي يربط خط أنابيب الـ RAG بالكامل في ملف واحد:
1. **Multi-Source Ingestion**: استقبال وتفريغ مستندات حقيقية من مجلد `data/` (TXT, PDF, Word, CSV).
2. **Text Splitting**: تقطيع المستندات باستخدام `RecursiveCharacterTextSplitter`.
3. **Remote Embeddings**: توليد متجهات التضمين عن بُعد سحابياً عبر نموذج `sentence-transformers/all-MiniLM-L6-v2` متوافق مع واجهة LangChain القياسية ودون أي اعتماد على PyTorch محلياً.
4. **Similarity Matrix**: مصفوفة تشابه كوزيني رقمية بين جمل من مجالات متنوعة (AI, Finance, Health).
5. **FAISS Vector Indexing**: بناء فهرس متجهات محلي فائق السرعة في الذاكرة.
6. **End-to-End Retrieval**: استرجاع المقاطع الأكثر صلة بالاستعلام مع درجات الثقة (Scores).
7. **2D Space Visualization**: إسقاط الفضاء الدلالي في بعدين عبر تفكيك القيم المنفردة النقي (`NumPy SVD / PCA`).

---

### 2. قسم الاستيراد والتفريغ ([`01-ingestion/`](01-ingestion/))
مخصص لتجربة ومعاينة أدوات التفريغ والقراءة لمختلف أنواع الملفات:
- **`01-text-parsing.ipynb`**: تجارب قراءة النصوص واستخدام الـ Text Loaders ومقارنة فواصل التقطيع.
- **`02-pdf-parsing.ipynb`**: مقارنة مكتبات قراءة الـ PDF (`PyPDF`, `PyMuPDF`).
- **`03-word-parsing.ipynb`**: استخراج محتوى مستندات Word المنسقة مع الجداول والفقرات.
- **`04-csv-excel-parsing.ipynb`**: تحويل صفوف الجداول إلى مستندات قابلة للفهرسة.
- **`05-json-parsing.ipynb`**: استخراج الحقول والعلاقات الهيكلية من ملفات الـ JSON.
- **`06-sql-parsing.ipynb`**: الاستعلام المباشر من قواعد بيانات SQLite وتحويل النتائج إلى وثائق.

---

### 3. قسم التضمينات الشعاعية ([`02-vector-embeddings/`](02-vector-embeddings/))
مخصص لتجربة أداء المتجهات وعمليات البحث والتشابه:
- اختبار نماذج التضمين السحابية `HuggingFaceAPIEmbeddings`.
- اختبار نماذج OpenAI Embeddings (`text-embedding-3-small`).
- حساب مصفوفات التشابه الكوزيني والمسافات المكانية ($L_2$).

---

### 4. قسم فهارس وقواعد بيانات المتجهات ([`03-vector-stores-and-databases/`](03-vector-stores-and-databases/))
مخصص لتجربة التخزين والاسترجاع السريع والفهرسة المتقدمة:
- **`01-vector-stores-vs-vector-databases.ipynb`**: مقارنة عملية دقيقة بين Vector Stores المدمجة (In-Memory) وقواعد البيانات السحابية، وقياس السرعة بالأجزاء من المليون من الثانية والتصفية بالبيانات الوصفية (Metadata Filtering).
- **`02-traditional-rag-chromadb.ipynb`**: بناء خط أنابيب الـ RAG الأولي وتجهيز النصوص بالـ DirectoryLoader والتجزئة الدلالية ثم الفهرسة في ChromaDB.
