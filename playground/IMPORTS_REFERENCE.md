# الموسوعة الشاملة لأحدث استيرادات ومعماريات RAG و AI Agents
### The Master Architecture & Modern Imports Reference (RAG, Advanced Retrieval, LangGraph & Agents)

تم إعداد هذا المرجع ليكون **الدليل المرجعي الكامل والمحدث لأحدث معايير عام 2025/2026**، ليغطي ليس فقط الاستيرادات البسيطة، بل **المعمارية الحديثة الكاملة لأنظمة RAG والوكلاء الأذكياء (Agentic RAG)** باستخدام أحدث إصدارات منظومة LangChain و LangGraph.

---

## 🧭 خارطة النقلة المعمارية الكبرى (The Modern Paradigm Shift)

شهدت منظومة الذكاء الاصطناعي انتقالاً جذرياً في طريقة بناء وتصميم الأنظمة:

```
[الحقبة القديمة: 2023]                        [المعمارية الحديثة: 2025/2026]
--------------------------------------------------------------------------------------
RetrievalQA                          --->     LCEL Pipelines (create_retrieval_chain)
ConversationalRetrievalChain         --->     create_history_aware_retriever + LCEL
AgentExecutor / initialize_agent     --->     LangGraph (StateGraph / create_react_agent)
ConversationBufferMemory             --->     LangGraph Checkpointers (MemorySaver / Postgres)
LLMChain                             --->     Pipe Operator: prompt | llm | parser
HuggingFaceHub                       --->     HuggingFaceEndpoint / Cloud Inference API
langchain.schema / vectorstores      --->     langchain_core / langchain_community
```

---

## 📑 الفهرس المعماري:

1. [المعمارية الأولى: خط أنابيب الـ RAG القياسي والمتقدم (Core & Advanced RAG)](#1-المعمارية-الأولى-خط-أنابيب-الـ-rag-القياسي-والمتقدم)
2. [المعمارية الثانية: الوكلاء الأذكياء والـ Agentic RAG باستخدام LangGraph](#2-المعمارية-الثانية-الوكلاء-الأذكياء-والـ-agentic-rag-باستخدام-langgraph)
3. [المعمارية الثالثة: أنماط الـ RAG المصححة ذاتيًا (CRAG & Self-RAG & Adaptive RAG)](#3-المعمارية-الثالثة-أنماط-الـ-rag-المصححة-ذاتيًا)
4. [المعمارية الرابعة: الرسوم المعرفية والـ GraphRAG](#4-المعمارية-الرابعة-الرسوم-المعرفية-والـ-graphrag)
5. [المعمارية الخامسة: التقييم والمراقبة المعيارية (Evaluation & Observability)](#5-المعمارية-الخامسة-التقييم-والمراقبة-المعيارية)
6. [الجدول المرجعي السريع: القديم (Deprecated) مقابل الحديث المعتمد (Modern)](#6-الجدول-المرجعي-السريع-القديم-مقابل-الحديث)

---

## 1. المعمارية الأولى: خط أنابيب الـ RAG القياسي والمتقدم

### 1.1 البنى الأساسية للوثائق (Document Core)
```python
from langchain_core.documents import Document

# تمثيل أي قطعة نصية مع بياناتها الوصفية
doc = Document(
    page_content="النص المسترجع أو المفرغ من الملف",
    metadata={"source": "annual_report.pdf", "page": 4, "category": "finance"}
)
```

---

### 1.2 تفريغ المستندات بجميع الصيغ (Document Loaders)
```python
from langchain_community.document_loaders import (
    TextLoader,        # للملفات النصية البسيطة: TextLoader("file.txt", encoding="utf-8")
    PyPDFLoader,       # لملفات الـ PDF وقراءتها صفحة بصفحة
    Docx2txtLoader,    # لمستندات Word (.docx)
    CSVLoader,         # لملفات الجداول CSV
    JSONLoader,        # لملفات JSON مع استعلام jq_schema
    SQLDatabaseLoader  # لاستخراج البيانات من جداول قواعد البيانات (SQLite/PostgreSQL)
)
```

---

### 1.3 خوارزميات التقطيع والتجزئة (Text Splitters)
```python
from langchain_text_splitters.character import (
    RecursiveCharacterTextSplitter, # الخوارزمية القياسية التنازلية الموصى بها
    CharacterTextSplitter           # التقطيع البسيط بفاصل محدد
)
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter # تقطيع حسب عناوين Markdown
from langchain_text_splitters.json import RecursiveJsonSplitter         # تقطيع كائنات الـ JSON المتشعبة

# الإعداد القياسي لـ RecursiveCharacterTextSplitter:
splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,        # أقصى حجم للمقطع
    chunk_overlap=50,      # التداخل بين المقاطع لمنع بتر السياق
    separators=["\n\n", "\n", ". ", " ", ""]
)
```

---

### 1.4 نماذج التضمين السحابية والمحلية (Embedding Models)
```python
# 1. التضمين السحابي المباشر عبر HuggingFace Endpoint (المعيار الرسمي لمكتبة langchain-huggingface)
from langchain_huggingface import HuggingFaceEndpointEmbeddings
hf_embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token=os.getenv("HF_TOKEN")
)

# 2. تضمينات OpenAI الرسمية
from langchain_openai import OpenAIEmbeddings
openai_embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
```

---

### 1.5 قواعد وفهارس المتجهات (Vector Stores)
```python
# 1. فهرس FAISS فائق السرعة في الذاكرة (In-Memory)
from langchain_community.vectorstores import FAISS

vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 2. قواعد متجهات أخرى شهيرة (Persistent):
# from langchain_community.vectorstores import Chroma, Qdrant
```

---

### 1.6 تقنيات الاسترجاع المتقدم (Advanced Retrieval Strategies)

#### أ. البحث الهجين (Hybrid Search = BM25 + Dense Vectors)
يجمع بين البحث بالكلمات المفتاحية (Keyword Matching) والبحث بالمتجهات الدلالية عبر خوارزمية **Reciprocal Rank Fusion (RRF)**:
```python
from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever

# 1. المفرس النصي (Sparse / Keyword)
bm25_retriever = BM25Retriever.from_documents(chunks)
bm25_retriever.k = 3

# 2. المفرس الدلالي (Dense / Vector)
dense_retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 3. الدمج الهجين بالأوزان
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, dense_retriever],
    weights=[0.4, 0.6]  # 40% كلمات مفتاحية، 60% تشابه دلالي
)
```

#### ب. استرجاع الوثائق الأم والأبناء (Parent Document Retriever)
البحث في مقاطع صغيرة دقيقة (Child Chunks)، وعند العثور عليها يتم إرسال الوثيقة الأصلية الأكبر (Parent Chunk) للـ LLM لضمان سياق كامل:
```python
from langchain_classic.retrievers import ParentDocumentRetriever
from langchain_core.stores import InMemoryByteStore

# تخزين المقاطع الأصلية في الذاكرة وفهرسة المقاطع الصغيرة في FAISS
store = InMemoryByteStore()
parent_retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    byte_store=store,
    child_splitter=RecursiveCharacterTextSplitter(chunk_size=200),
    parent_splitter=RecursiveCharacterTextSplitter(chunk_size=1000)
)
```

#### ج. إعادة الترتيب وإعادة التصفية (Reranking & Contextual Compression)
```python
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_community.document_compressors import FlashrankRerank  # أو CohereRerank

# إعادة ترتيب المقاطع المسترجعة باستخدام Cross-Encoder لرفع الدقة
compressor = FlashrankRerank()
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vectorstore.as_retriever(search_kwargs={"k": 10})
)
```

---

### 1.7 بناء خط أنابيب الـ RAG بنمط LCEL الحديث
بديل `RetrievalQA` المتقادم:
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

# 1. إعداد النموذج والمحفز
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

prompt = ChatPromptTemplate.from_template("""
أجب عن السؤال بناءً على السياق المسترجع فقط:
السياق: {context}
السؤال: {question}
الإجابة:
""")

# 2. دالة تجميع نصوص المقاطع
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 3. خط الأنابيب المتكامل بنمط LCEL
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

response = rag_chain.invoke("ما هي مزايا نظام RAG؟")
```

---

## 2. المعمارية الثانية: الوكلاء الأذكياء والـ Agentic RAG باستخدام LangGraph

> [!IMPORTANT]
> **وداعًا لـ `AgentExecutor`**: أعلنت LangChain رسميًا إيقاف تطوير `AgentExecutor` والانتقال الكامل إلى **LangGraph** لبناء الوكلاء الأذكياء والـ ReAct Agents وإدارة الحالات والذاكرة.

### 2.1 بنية LangGraph الأساسية (Core Graph Architecture)
```python
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition, create_react_agent
from langgraph.checkpoint.memory import MemorySaver  # الذاكرة وحفظ الحالة
```

---

### 2.2 تعريف الأدوات (Tools Definition)
في الـ Agentic RAG، يكون "الاسترجاع" (Retrieval) عبارة عن أداة (`tool`) يستدعيها الوكيل وقتما يرى ذلك ضرورياً:
```python
from langchain_core.tools import tool
from pydantic import BaseModel, Field

# تعريف أداة الاسترجاع للوكيل
@tool
def search_knowledge_base(query: str) -> str:
    """ابحث في قاعدة المعرفة التقنية الخاصة بالشركة عن إجابات دقيقة."""
    docs = retriever.invoke(query)
    return "\n\n".join(d.page_content for d in docs)

# أداة حسابية إضافية
@tool
def calculate_growth_rate(initial: float, final: float) -> str:
    """احسب نسبة النمو المئوية بين قيمتين."""
    growth = ((final - initial) / initial) * 100
    return f"نسبة النمو هي {growth:.2f}%"

tools = [search_knowledge_base, calculate_growth_rate]
```

---

### 2.3 بناء وكيل ReAct تفاعلي مع الذاكرة (Production ReAct Agent)
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

# 1. نظام حفظ الذاكرة للجلسات المتعددة (Checkpointer)
memory = MemorySaver()

# 2. إنشاء الوكيل الذكي بنمط LangGraph المعياري
agent = create_react_agent(
    model=llm,
    tools=tools,
    checkpointer=memory,
    state_modifier="أنت وكيل ذكاء اصطناعي خبير. استخدم أداة البحث لاسترجاع المعلومات قبل الإجابة."
)

# 3. استدعاء الوكيل مع معرّف الجلسة (Thread ID) لحفظ سجل المحادثة
config = {"configurable": {"thread_id": "session-user-101"}}

response = agent.invoke(
    {"messages": [("user", "ما هي تفاصيل التقرير المالي لسنة 2026 وما نسبة نمو الأرباح؟")]},
    config=config
)

print(response["messages"][-1].content)
```

---

### 2.4 ربط الأدوات وتوليد المخرجات المنظمة (Structured Outputs)
```python
from pydantic import BaseModel, Field

class RAGDecision(BaseModel):
    """قرار الوكيل بشأن جودة الاسترجاع."""
    is_relevant: bool = Field(description="هل السياق المسترجع يحتوي على إجابة السؤال؟")
    reasoning: str = Field(description="السبب وراء هذا القرار")

# إجبار النموذج على إرجاع كائن Pydantic منظم دائمًا
structured_llm = llm.with_structured_output(RAGDecision)
decision = structured_llm.invoke("السياق يحتوي على تعريف التعلم العميق، والسؤال عن الذكاء الاصطناعي.")
print(decision.is_relevant)
```

---

## 3. المعمارية الثالثة: أنماط الـ RAG المصححة ذاتيًا

تعتمد أنظمة RAG المتقدمة على التدقيق الذاتي:
- **CRAG (Corrective RAG)**: تقييم الوثائق المسترجعة، وإذا كانت ضعيفة، تفعيل البحث في الويب (Web Search fallback).
- **Self-RAG**: تقييم إجابة النموذج للتأكد من عدم وجود هلوسة (Hallucination Grading).
- **Adaptive RAG**: توجيه الاستعلام (Query Routing) للمسار الأنسب.

### مكونات بناء Graph التصحيح الذاتي في LangGraph:
```python
from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END

# 1. تعريف حالة الرسم البياني (Graph State)
class GraphState(TypedDict):
    question: str
    documents: List[Document]
    generation: str
    web_search_needed: bool

# 2. دوال العقد (Nodes)
def retrieve_node(state: GraphState):
    """استرجاع الوثائق من الفهرس"""
    docs = retriever.invoke(state["question"])
    return {"documents": docs}

def grade_documents_node(state: GraphState):
    """تقييم صلة الوثائق المسترجعة بالسؤال"""
    # كود التحقق وتعيين web_search_needed = True إذا كانت الوثائق غير مفيدة
    return {"web_search_needed": False}

def generate_node(state: GraphState):
    """توليد الإجابة"""
    return {"generation": "الإجابة المولدة بناءً على السياق المصحح"}

# 3. الشروط التفرعية (Conditional Edges)
def decide_to_generate(state: GraphState):
    if state["web_search_needed"]:
        return "web_search"
    return "generate"

# 4. تجميع الـ StateGraph
workflow = StateGraph(GraphState)
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("grade_docs", grade_documents_node)
workflow.add_node("generate", generate_node)

workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "grade_docs")
workflow.add_conditional_edges(
    "grade_docs",
    decide_to_generate,
    {"web_search": "retrieve", "generate": "generate"}
)
workflow.add_edge("generate", END)

crag_app = workflow.compile()
```

---

## 4. المعمارية الرابعة: الرسوم المعرفية والـ GraphRAG

لدمج قواعد البيانات المترابطة (Knowledge Graphs) واسترجاع العلاقات المعقدة بين الكيانات:

```python
from langchain_community.graphs import Neo4jGraph
from langchain_community.chains.graph_qa.cypher import GraphCypherQAChain

# 1. الاتصال بقاعدة بيانات Neo4j
graph = Neo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="password"
)

# 2. سلسلة توليد استعلامات Cypher واسترجاع العلاقات المعرفية
chain = GraphCypherQAChain.from_llm(
    llm=llm,
    graph=graph,
    verbose=True,
    allow_dangerous_requests=True
)

response = chain.invoke({"query": "ما هي الشركات التابعة التي يستثمر فيها أحمد؟"})
```

---

## 5. المعمارية الخامسة: التقييم والمراقبة المعيارية

### 5.1 التتبع والمراقبة اللحظية (LangSmith Tracing)
لا تحتاج لأكواد معقدة، فقط تفعيل المتغيرات في بيئة العمل:
```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "lsv2_pt_..."
os.environ["LANGCHAIN_PROJECT"] = "rag-mastery-production"
```

### 5.2 مقاييس جودة الـ RAG المعيارية (RAGAS Metrics)
```python
# أشهر مكتبة لتقييم أنظمة RAG بالأرقام المعيارية
# pip install ragas
from ragas import evaluate
from ragas.metrics import (
    faithfulness,        # قياس الهلوسة: هل الإجابة مبنية على السياق؟
    answer_relevancy,    # هل الإجابة ترد على سؤال المستخدم بدقة؟
    context_precision,   # هل المقاطع المسترجعة دقيقة وخالية من الحشو؟
    context_recall       # هل استرجع النظام كل المعلومات اللازمة للإجابة؟
)
```

---

## 6. الجدول المرجعي السريع: القديم مقابل الحديث

| المكون (Component) | المسار القديم المتقادم ❌ (Deprecated) | المسار الحديث المعتمد 100% ✔️ (Modern) |
| :--- | :--- | :--- |
| **Document** | `from langchain.schema import Document` | `from langchain_core.documents import Document` |
| **Embeddings Base** | `from langchain.embeddings.base import Embeddings` | `from langchain_core.embeddings import Embeddings` |
| **Retriever Base** | `from langchain.schema import BaseRetriever` | `from langchain_core.retrievers import BaseRetriever` |
| **PromptTemplate** | `from langchain.prompts import PromptTemplate` | `from langchain_core.prompts import PromptTemplate` |
| **ChatPromptTemplate**| `from langchain.prompts import ChatPromptTemplate` | `from langchain_core.prompts import ChatPromptTemplate` |
| **Output Parser** | `from langchain.schema.output_parser import StrOutputParser` | `from langchain_core.output_parsers import StrOutputParser` |
| **Messages** | `from langchain.schema import HumanMessage, AIMessage` | `from langchain_core.messages import HumanMessage, AIMessage` |
| **Recursive Splitter**| `from langchain.text_splitter import RecursiveCharacterTextSplitter` | `from langchain_text_splitters.character import RecursiveCharacterTextSplitter` |
| **Text Loader** | `from langchain.document_loaders import TextLoader` | `from langchain_community.document_loaders import TextLoader` |
| **PDF Loader** | `from langchain.document_loaders import PyPDFLoader` | `from langchain_community.document_loaders import PyPDFLoader` |
| **FAISS Store** | `from langchain.vectorstores import FAISS` | `from langchain_community.vectorstores import FAISS` |
| **OpenAI LLM** | `from langchain.chat_models import ChatOpenAI` | `from langchain_openai import ChatOpenAI` |
| **OpenAI Embeddings** | `from langchain.embeddings import OpenAIEmbeddings` | `from langchain_openai import OpenAIEmbeddings` |
| **HuggingFace API** | `from langchain.llms import HuggingFaceHub` | `from langchain_huggingface import HuggingFaceEndpoint` |
| **HuggingFace Embed**| `from langchain.embeddings import HuggingFaceEmbeddings` | `from langchain_huggingface import HuggingFaceEndpointEmbeddings` |
| **Chains / QA** | `from langchain.chains import RetrievalQA` | نمط **LCEL Pipelines** أو **LangGraph** |
| **Agents Engine** | `from langchain.agents import AgentExecutor, initialize_agent` | `from langgraph.prebuilt import create_react_agent` أو `StateGraph` |
| **Memory Buffer** | `from langchain.memory import ConversationBufferMemory` | `from langgraph.checkpoint.memory import MemorySaver` |
| **Tools Definition** | `from langchain.agents import tool` | `from langchain_core.tools import tool` |

---

## 💡 كيف تستخدم هذا المرجع في عملك اليومي؟
1. افتح هذا الملف كـ Cheat Sheet بجانب شاشة كتابة الأكواد.
2. لأي مرحلة في الـ RAG، انسخ المسار الحديث وتفادى تماماً أي استيرادات قديمة من شروحات 2023.
3. لأي خطوة في بناء الـ Agents، استخدم **LangGraph** (`StateGraph`, `create_react_agent`, `@tool`).
