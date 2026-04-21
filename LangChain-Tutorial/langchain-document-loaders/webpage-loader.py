from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# It uses two other python libraries to load the data - requests (for http requests) and BeautifulSoup (html structure).
# It is modtly used for static pages (HTML Heavy)
# Use SelemiumURLLOader for dynamic (JS Heavy) Web pages

url = 'https://www.amazon.in/dp/B0DSKL9MQ8?ref_=TopBrands_AL_1&pf_rd_r=0AACC47739754008A39F&pf_rd_p=ac2a536d-4d89-4d94-8b75-24f9fc1b9cf5&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-8_CW&pf_rd_t=&pf_rd_i=1389401031'

loader = WebBaseLoader(url)

doc = loader.load()

# Each url is listed as a single chunk.
# We can also pass a list of URLs to get data from mutliple sources
print(len(doc))
print(doc[0].metadata)


load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template='Answer the question from the following text\nText:{text}\nQuestion:{query}',
    input_variables=['text','query']
)

chain = prompt | model | parser

print(chain.invoke({'text':doc[0].page_content,'query':'Tell me the name and price of this product?'}))
