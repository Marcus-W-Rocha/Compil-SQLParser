class SQLParser:
    def __init__(self, query):
        self.query = query
        self.tokens = self.tokenize(query)
        self.current_token = None
        self.current_index = -1
        self.next_token()

    def tokenize(self, query):
        # Implemente a função de tokenização para dividir a consulta em tokens
        # Aqui está um exemplo simples para fins de demonstração:
        return query.split()

    def next_token(self):
        self.current_index += 1
        if self.current_index < len(self.tokens):
            self.current_token = self.tokens[self.current_index]
        else:
            self.current_token = None

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.next_token()
        else:
            raise SyntaxError(f"Token inesperado: {self.current_token}")

    def parse(self):
        self.statement()

    def statement(self):
        if self.current_token == "CREATE":
            self.create_statement()
        elif self.current_token == "USE":
            self.select_statement()
        elif self.current_token == "INSERT":
            self.insert_statement()
        elif self.current_token == "SELECT":
            self.select_statement()
        elif self.current_token == "UPDATE":
            self.update_statement()
        elif self.current_token == "DELETE":
            self.delete_statement()
        elif self.current_token == "TRUNCATE":
            self.truncate_statement()
        else:
            raise SyntaxError(f"Comando SQL inválido: {self.current_token}")

    def create_statement(self):
        self.match("CREATE")
        # Implemente a lógica para analisar um comando CREATE

    def create_statement(self):
        self.match("USE")
        # Implemente a lógica para analisar um comando CREATE

    def insert_statement(self):
        self.match("INSERT")
        # Implemente a lógica para analisar um comando INSERT

    def select_statement(self):
        self.match("SELECT")
        # Implemente a lógica para analisar um comando SELECT

    def update_statement(self):
        self.match("UPDATE")
        # Implemente a lógica para analisar um comando UPDATE

    def delete_statement(self):
        self.match("DELETE")
        # Implemente a lógica para analisar um comando DELETE

    def truncate_statement(self):
        self.match("TRUNCATE")
        # Implemente a lógica para analisar um comando TRUNCATE

# Exemplo de uso
query = "SELECT * FROM table_name"
parser = SQLParser(query)
parser.parse()