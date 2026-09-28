# 01 - إعداد بيئة العمل وهيكل المشروع باستخدام UV (Project Setup with UV)

> **ملخص سريع:** المحاضرة التاسعة من الكورس (المحاضرة الأولى في قسم الـ Ingestion). تركز على تأسيس بيئة عمل برمجية احترافية وسريعة جداً باستخدام مدير الحزم الحديث **UV** المبني بلغة Rust، وتثبيت حزم منظومة LangChain والمكتبات الأساسية للـ Ingestion.

---

## 1. ما هو مدير الحزم UV؟ ولماذا نستخدمه؟ (Why UV?)

في بيئات تطوير الذكاء الاصطناعي السابقة، كان الاعتماد الأكبر على `pip` أو `conda` أو `poetry`، ولكن مع ضخامة مكتبات الـ AI (مثل PyTorch و Transformers):
* **UV** هو مدير حزم ومشاريع حديث ومفتوح المصدر طُوّر بواسطة Astral، ومكتوب بلغة **Rust**.
* **السرعة الخارقة:** أسرع من `pip` بحوالي **10 إلى 100 ضعف** بفضل التوازي الذكي وإدارة الـ Cache بلغة Rust.
* **إدارة متكاملة:** بديل شامل يجمع إمكانيات `pip` و `virtualenv` و `pip-tools` وإدارة إصدارات بايثون المتعددة في أداة واحدة موحدة.

---

## 2. خطوات التثبيت والإعداد خطوة بخطوة (Step-by-Step Setup)

### ① تثبيت أداة UV على نظام التشغيل:
* **عبر PowerShell (Windows):**
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
* **أو عبر pip مباشرة:**
  ```bash
  pip install uv
  ```

---

### ② تهيئة المشروع وإنشاء البيئة الافتراضية:
1. **تهيئة مجلد المشروع:**
   ```bash
   uv init
   ```
   *يولد هذا الأمر ملف `pyproject.toml` لتوثيق المشروع وتبعيّاته.*

2. **إنشاء البيئة الافتراضية (Virtual Environment):**
   ```bash
   uv venv
   ```
   *(أو تحديد إصدار بايثون محدد: `uv venv --python 3.12` أو `3.13`)*

3. **تفعيل البيئة الافتراضية (Activation):**
   * **على Windows (PowerShell / CMD):**
     ```powershell
     .venv\Scripts\activate
     ```
   * **على Linux / Mac:**
     ```bash
     source .venv/bin/activate
     ```

---

## 3. مكتبات منظومة LangChain والـ Ingestion (Core Dependencies)

تم تجهيز قائمة المكتبات المطلوبة للقسم بالكامل:

| المكتبة (Library) | الدور الوظيفي في منظومة RAG |
| :--- | :--- |
| **`langchain`** | الإطار الأساسي لبناء سلاسل ومسارات الـ RAG عبر LCEL. |
| **`langchain-community`** | محولات التحميل والتكامل الخارجي (Document Loaders, Vector Stores). |
| **`langchain-openai`** | الاتصال بنماذج التوليد والتضمين من OpenAI (GPT-4o, Text-Embedding-3). |
| **`langchain-groq`** | استضافة وتشغيل النماذج مفتوحة المصدر (Llama 3) بسرعة استدلال خارقة. |
| **`faiss-cpu`** | محرك بحث متجهات محلي فائق السرعة مطور من Meta. |
| **`sentence-transformers`** | نماذج تضمين دلالي محلية ومجانية من منصة Hugging Face. |
| **`tiktoken`** | حساب عدد الـ Tokens وتقسيم النصوص بدقة متوافقة مع النماذج. |
| **`pypdf`** | قراءة واستخراج النصوص والصفحات من ملفات PDF. |
| **`python-dotenv`** | إدارة وتأمين مفاتيح الـ API السرية عبر ملف `.env`. |
| **`ipykernel`** | تشغيل دفاتر Jupyter Notebook داخل البيئة الافتراضية. |

---

### ③ تثبيت التبعيات باستخدام UV:

بدلاً من أمر `pip install -r requirements.txt`، نستخدم أمر `uv`:

```bash
uv add -r requirements.txt
uv add ipykernel
```

---

## 4. ملف المتغيرات البيئية (`.env`)

يُستخدم لحفظ مفاتيح الوصول بأمان دون تضمينها في الكود:
```env
OPENAI_API_KEY="sk-..."
GROQ_API_KEY="gsk_..."
```

---

## 5. اختبار الاتصال بالبيئة (Verification)

داخل دفتر الملاحظات المرفق [`01-environment-setup.ipynb`](./01-environment-setup.ipynb)، يتم التحقق من صحة التثبيت بتنفيذ:
```python
import langchain
import langchain_community
import faiss
import pypdf

print(f"✅ LangChain Version: {langchain.__version__}")
print("✅ All core ingestion libraries imported successfully!")
```
