class MetaData(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # if request.user.is_authenticated:
        #     message = 'Olá %s, Bom dia!' % request.user.username 
        # else:
        #     message = 'Olá Bom dia!'
        
        request.session['message'] = 'Mensagem do middleware'
        print(f"request middleware= {request.session['message']}")

        return None
