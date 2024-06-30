(this["webpackJsonpeco-friendly-ai-selector"]=this["webpackJsonpeco-friendly-ai-selector"]||[]).push([[0],{39:function(e,t,r){"use strict";r.r(t);var o=r(1),s=r.n(o),c=r(13),a=r.n(c),n=r(14),l=r.n(n),d=r(0);var i=e=>{let{query:t,setQuery:r,error:o,setError:s,sendQuery:c}=e;return Object(d.jsxs)("div",{className:"mb-6",children:[Object(d.jsx)("label",{htmlFor:"query",className:"block text-sm font-medium text-gray-700 mb-2",children:"Enter your query"}),Object(d.jsx)("input",{id:"query",type:"text",value:t,onChange:e=>{r(e.target.value),""===e.target.value.trim()?s("Query cannot be empty"):s("")},placeholder:"What would you like to know?",className:"w-full p-3 border rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 ".concat(o?"border-red-500":"border-gray-300")}),o&&Object(d.jsx)("p",{className:"mt-2 text-sm text-red-600",children:o}),Object(d.jsx)("button",{onClick:c,className:"mt-4 w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 transition-colors",children:"Calculate"})]})};var u=e=>{let{selectedModel:t,setSelectedModel:r,handleSearch:o,isLoading:s}=e;return Object(d.jsx)("div",{className:"grid grid-cols-1 md:grid-cols-3 gap-6 mb-6",children:["google","chatgpt","mistral"].map((e=>Object(d.jsxs)("div",{className:"border border-gray-200 p-4 rounded-md shadow-sm hover:shadow-md transition-shadow",children:[Object(d.jsx)("h2",{className:"text-xl font-bold mb-3 capitalize",children:e}),Object(d.jsxs)("button",{onClick:()=>{r(e),o(e)},disabled:s,className:"w-full py-2 px-4 rounded-md transition-colors ".concat(t===e?"bg-indigo-600 text-white hover:bg-indigo-700":"bg-gray-200 text-gray-700 hover:bg-gray-300"),children:["Use ",e]})]},e)))})};var b=e=>{let{result:t}=e;return Object(d.jsx)("pre",{children:JSON.stringify(t,null,2)})};var g=e=>{let{message:t}=e;return Object(d.jsx)("div",{className:"bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative",role:"alert",children:Object(d.jsx)("span",{className:"block sm:inline",children:t})})};var h={API_URL:"http://127.0.0.1:8000"};var m=()=>{const[e,t]=Object(o.useState)(""),[r,s]=Object(o.useState)(""),[c,a]=Object(o.useState)(null),[n,m]=Object(o.useState)(null),[j,p]=Object(o.useState)(null),[y,x]=Object(o.useState)(!1);return Object(d.jsxs)("div",{className:"container mx-auto p-4",children:[Object(d.jsx)("h1",{className:"text-3xl font-bold mb-4",children:"Eco-Friendly AI Model Selector"}),Object(d.jsx)(i,{query:e,setQuery:t}),Object(d.jsx)(u,{selectedModel:r,setSelectedModel:s,handleSearch:async t=>{console.log("Searching with model: ".concat(t)),console.log("Searching at: ".concat(h.API_URL,"/query/")),x(!0),p(null),console.log("Trying to get response...");try{if("chatgpt"===t)window.open("https://chat.openai.com/","_blank"),a({result:"Please use your ChatGPT account to process this query: "+e,ecoMetrics:{energyUsage:"N/A",treesSaved:"N/A",drivingAvoided:"N/A"}});else{const r=await l()({method:"post",url:"".concat(h.API_URL,"/query/"),data:{query:e,model:t,conversationId:n},headers:{"Content-Type":"application/json",Accept:"application/json"},withCredentials:!0});console.log("Received response..."),console.log("Response:",r.data),a(r.data),m(r.data.conversationId)}}catch(j){console.error("Error:",j.response?j.response.data:j.message),p("An error occurred while processing your request. Please try again.")}finally{x(!1)}console.log("Search process completed.")},isLoading:y,query:e,conversationId:n}),j&&Object(d.jsx)(g,{message:j}),c&&Object(d.jsx)(b,{result:c})]})};a.a.render(Object(d.jsx)(s.a.StrictMode,{children:Object(d.jsx)(m,{})}),document.getElementById("root"))}},[[39,1,2]]]);
//# sourceMappingURL=main.84f849c0.chunk.js.map