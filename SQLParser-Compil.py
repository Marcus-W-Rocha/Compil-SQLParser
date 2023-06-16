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
        if self.current_token == "USE":
            self.select_statement()
        elif self.current_token == "CREATE":
            self.create_statement()
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

    def where(self):
        self.match("WHERE")
        self.match(coluna)
        self.match(operador)
        self.match(valor)
        
    def use_statement(self):
        self.match("USE")
        self.match(tabela)
        self.match(";")
        # Implemente a lógica para analisar um comando USE

    def create_statement(self):
        self.match("CREATE")
        if self.current_token == "DATABASE":
            self.match("DATABASE")
            self.match(banco)
            self.match(";")
        if self.current_token == "TABLE":
            self.match("TABLE")
            self.match(tabela)
            self.match("(")
            self.match(coluna)
            self.match(tipoDado)

            self.match(",")
            self.match(coluna)
            self.match(tipoDado)
            #colocar essa parte em loop de alguma forma (no texto prof coloca * )

            self.match(")")
            self.match(";")
        # Implemente a lógica para analisar um comando CREATE

    def insert_statement(self):
        self.match("INSERT")
        self.match("INTO")
        self.match(tabela)
        self.match("(")
        self.match(coluna)

        self.match(",")
        self.match(coluna)
        #colocar essa parte em loop de alguma forma (no texto prof coloca * )
        self.match(")")

        self.match("VALUES")
        self.match("(")
        self.match(valor)

        self.match(",")
        self.match(valor)
        #colocar essa parte em loop de alguma forma (no texto prof coloca * )

        self.match(")")

        # Implemente a lógica para analisar um comando INSERT

    def select_statement(self):
        self.match("SELECT")
        if self.current_token == "*":
            self.match("*")
            self.match("FROM")
            self.match(tabela)
            if self.current_token == "ORDER":
                self.match("ORDER")
                self.match("BY")
                self.match("BY")
                self.match(coluna)
            elif self.current_token == "WHERE":
                self.match("WHERE")
                self.match(coluna)
                self.match(operator)
                self.match(valor)
        if self.current_token == coluna:
           self.match(coluna)

           self.match(coluna)
           #colocar essa parte em loop de alguma forma (no texto prof coloca * )

           self.match("FROM")
           self.match(coluna)
        self.match(";") 

        
        # Implemente a lógica para analisar um comando SELECT

    def update_statement(self):
        self.match("UPDATE")
        self.match(tabela)
        self.match("SET")
        self.match(coluna)
        self.match(operator)
        self.match(valor)

        if self.current_token == "WHERE":
            self.where()
        # Implemente a lógica para analisar um comando UPDATE
        self.match(";")

    def delete_statement(self):
        self.match("DELETE")
        self.match("FROM")
        self.match(tabela)

        if  self.current_token == "WHERE":
            self.where()
        # Implemente a lógica para analisar um comando DELETE
        self.match(";")
   
    def truncate_statement(self):
        self.match("TRUNCATE")
        self.match("TABLE")
        self.match(tabela)
        self.match(";")

# Exemplo de uso
query = "SELECT * FROM table_name"
parser = SQLParser(query)
parser.parse()