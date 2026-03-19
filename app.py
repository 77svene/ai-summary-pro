
    import gradio as gr
    import requests
    
    # OpenRouter API Configuration
    OPENROUTER_API_KEY = "openrouter_key" # Injected via environment or config
    OPENROUTER_MODEL = "openrouter_model"
    
    def summarize(text, max_length=150):
        if not text:
            return "Please enter some text to summarize."
        try:
            payload = {
                "model": OPENROUTER_MODEL,
                "messages": [
                    {
                        "role": "user",
                        "content": f"Summarize the following text concisely in {max_length} words or less:\n\n{text}"
                    }
                ]
            }
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload)
            if response.status_code == 200:
                data = response.json()
                summary = data["choices"][0]["message"]["content"]
                return summary
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error processing: {str(e)}"
    
    with gr.Blocks() as demo:
        gr.Markdown("# AI Summary Pro")
        with gr.Row():
            inp = gr.Textbox(label="Input Text", lines=10, placeholder="Paste long text here...")
            btn = gr.Button("Summarize")
        out = gr.Textbox(label="Summary", lines=5)
        btn.click(summarize, inp, out)
    
    demo.launch(server_name="0.0.0.0", server_port=7860)
    

# Added optimized prompt for better summaries
optimized_prompt = """Summarize the text concisely while retaining key points."""

async def summarize(self, text):
    prompt = optimized_prompt
    # ... existing logic ...
    return prompt
