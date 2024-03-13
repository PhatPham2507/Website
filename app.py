from flask import Flask, render_template, request
from bartphoWeb import bartpho_generate_summary_short, bartpho_generate_summary_medium, bartpho_generate_summary_long,error_message, bartpho_tokenizer,bartpho_model
from vit5Web import vit5_generate_summary_short, vit5_generate_summary_medium, vit5_generate_summary_long, viT5_tokenizer, viT5_model
# from mt5Web import mt5_generate_summary_short, mt5_generate_summary_medium, mt5_generate_summary_long, mt5_model, mt5_tokenizer
# from mbartWeb import mbart_generate_summary_short, mbart_generate_summary_medium, mbart_generate_summary_long, mbart_model, mbart_tokenizer

app = Flask(__name__)

# Tải mô hình và lưu vào biến toàn cục

bartpho_tokenizer = bartpho_tokenizer
bartpho_model = bartpho_model
# Tạo biến toàn cục để lưu trữ tokenizer
viT5_tokenizer = viT5_tokenizer
viT5_model = viT5_model

# mt5_model = mt5_model
# mt5_tokenizer = mt5_tokenizer

# mbart_model = mbart_model
# mbart_tokenizer = mbart_tokenizer

def load_or_get_model(model_name):
    """
    Hàm này trả về mô hình từ biến toàn cục tương ứng với tên mô hình.
    """
    if model_name == 'bartPho':
        return bartpho_model
    elif model_name == 'ViT5':
        return viT5_model
    
    # if model_name == 'mT5':
    #     return mt5_model
    # if model_name == 'mBart':
    #     return mbart_model
    
    
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        summary_length = request.form['summary_length']
        model_selection = request.form['model_select']

        model = load_or_get_model(model_selection)

        if  summary_length == "Select Summary Length" or model_selection == "Select Model":
            summary = error_message(model, bartpho_tokenizer, input_text, max_length = 0)
            return render_template('index.html', input_text=input_text, summary=summary)
        
        else:
            if model_selection == 'bartPho':
                if summary_length == 'short':
                    max_length = 100
                    summary = bartpho_generate_summary_short(model, bartpho_tokenizer, input_text, max_length)

                elif summary_length == 'medium':
                    max_length = 200
                    summary = bartpho_generate_summary_medium(model, bartpho_tokenizer, input_text, max_length)
                elif summary_length == 'long':
                    max_length = 300
                    summary = bartpho_generate_summary_long(model, bartpho_tokenizer, input_text, max_length)
                else:
                    summary = "Invalid summary length"
                
                return render_template('index.html', input_text=input_text, summary=summary) 
            
            elif model_selection == 'ViT5':
                if summary_length == 'short':
                    max_length = 100
                    summary = vit5_generate_summary_short(model, viT5_tokenizer, input_text, max_length)

                elif summary_length == 'medium':
                    max_length = 200
                    summary = vit5_generate_summary_medium(model, viT5_tokenizer, input_text, max_length)
                elif summary_length == 'long':
                    max_length = 300
                    summary = vit5_generate_summary_long(model, viT5_tokenizer, input_text, max_length)
                else:
                    summary = "Invalid summary length"
                
                return render_template('index.html', input_text=input_text, summary=summary)
            # if model_selection == 'mT5':
            #     if summary_length == 'short':
            #         max_length = 100
            #         summary = mt5_generate_summary_short(mt5_model, mt5_tokenizer, input_text, max_length)

            #     elif summary_length == 'medium':
            #         max_length = 200
            #         summary = mt5_generate_summary_medium(mt5_model, mt5_tokenizer, input_text, max_length)
            #     elif summary_length == 'long':
            #         max_length = 300
            #         summary = mt5_generate_summary_long(mt5_model, mt5_tokenizer, input_text, max_length)
            #     else:
            #         summary = "Invalid summary length"
                
            #     return render_template('index.html', input_text=input_text, summary=summary)
            
        # if model_selection == 'mBart':
        #             if summary_length == 'short':
        #                 max_length = 100
        #                 summary = mbart_generate_summary_short(mbart_model, mbart_tokenizer, input_text, max_length)
        #             elif summary_length == 'medium':
        #                 max_length = 200
        #                 summary = mbart_generate_summary_medium(mbart_model, mbart_tokenizer, input_text, max_length)
        #             elif summary_length == 'long':
        #                 max_length = 300
        #                 summary = mbart_generate_summary_long(mbart_model, mbart_tokenizer, input_text, max_length)
        #             else:
        #                 summary = "Invalid summary length"
                    
        #             return render_template('index.html', input_text=input_text, summary=summary)      
                

    return render_template('index.html')

if __name__ == '_main_':
    app.run(debug=True)