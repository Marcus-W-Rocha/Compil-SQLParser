class SQLParser:
    def __init__(self, query):
        self.query = query
        self.tokens = self.criarTokens(query)
        self.token_atual = None
        self.index_atual = -1
        self.nextToken()

    def criarTokens(self, query):
        query = query[:-1]
        query = query + " ;"
        query = query.strip()
        delimitadores = ["(",")",","," "]
        tokens= []
        token_atual = ""
        aspas = False

        for a in query:
            if a == "'":
                aspas = not aspas
                token_atual += a
            elif a in delimitadores and not aspas:
                if token_atual:
                    tokens.append(token_atual)
                token_atual= ""
                if a != " ":
                    tokens.append(a)
            else:
                token_atual += a
        
        if token_atual:
            tokens.append(token_atual)
        return tokens

    def nextToken(self):
        self.index_atual += 1
        if self.index_atual < len(self.tokens):
            self.token_atual = self.tokens[self.index_atual]
        else:
            self.token_atual = None

    def match(self, expected_token):
        if self.token_atual == expected_token:
            self.nextToken()
        else:
            raise SyntaxError(f"Token inesperado: {self.token_atual}")

    def parse(self):
        self.statement()

    def statement(self):
        if self.token_atual == "USE":
            self.select_statement()
        elif self.token_atual == "CREATE":
            self.create_statement()
        elif self.token_atual == "INSERT":
            self.insert_statement()
        elif self.token_atual == "SELECT":
            self.select_statement()
        elif self.token_atual == "UPDATE":
            self.update_statement()
        elif self.token_atual == "DELETE":
            self.delete_statement()
        elif self.token_atual == "TRUNCATE":
            self.truncate_statement()
        else:
            raise SyntaxError(f"Comando SQL inválido: {self.token_atual}")

    def where(self):
        self.match("WHERE")
        self.match("<id>")
        self.match("=")
        self.match("<valor>")
        
    def use_statement(self):
        self.match("USE")
        self.match("<id>")
        self.match(";")
# Implemente a lógica para analisar um comando USE

    def create_statement(self):
        self.match("CREATE")
        if self.token_atual == "DATABASE":
            self.match("DATABASE")
            self.match("<id>")

        if self.token_atual == "TABLE":
            self.match("TABLE")
            self.match("<id>")
            self.match("(")
            self.match("<id>")
            self.match("<tipo>")

            while self.token_atual == ",":
                self.match(",")
                self.match("<id>")
                self.match("<tipo>")

            self.match(")")
        self.match(";")
# Implemente a lógica para analisar um comando CREATE

    def insert_statement(self):
        self.match("INSERT")
        self.match("INTO")
        self.match("<id>")
        self.match("(")
        self.match("<id>")

        while self.token_atual == ",":
            self.match(",")
            self.match("<id>")
        self.match(")")

        self.match("VALUES")
        self.match("(")
        self.match("<valor>")

        while self.token_atual == ",":
            self.match(",")
            self.match("<valor>")

        self.match(")")
        self.match(";")
# Implemente a lógica para analisar um comando INSERT

    def select_statement(self):
        self.match("SELECT")
        if self.token_atual == "*":
            self.match("*")
            self.match("FROM")
            self.match("<id>")
            if self.token_atual == "ORDER":
                self.match("ORDER")
                self.match("BY")
                self.match("<id>")
            elif self.token_atual == "WHERE":
                self.where()

        if self.token_atual == "<id>":
           self.match("<id>")
           while self.token_atual == ",":
               self.match(",")
               self.match("<id>")
           self.match("FROM")
           self.match("<id>")
        self.match(";") 
# Implemente a lógica para analisar um comando SELECT

    def update_statement(self):
        self.match("UPDATE")
        self.match("<id>")
        self.match("SET")
        self.match("<id>")
        self.match("=")
        self.match("<valor>")

        if self.token_atual == "WHERE":
            self.where()
        self.match(";")
# Implemente a lógica para analisar um comando UPDATE

    def delete_statement(self):
        self.match("DELETE")
        self.match("FROM")
        self.match("<id>")

        if  self.token_atual == "WHERE":
            self.where()
        self.match(";")
# Implemente a lógica para analisar um comando DELETE
   
    def truncate_statement(self):
        self.match("TRUNCATE")
        self.match("TABLE")
        self.match("<id>")
        self.match(";")
# Implemente a lógica para analisar um comando TRUNCATE

# Exemplo de uso
query = "SELECT <id>, <id>, <id>, <id> FROM <id> ;"
parser = SQLParser(query)
parser.parse()
print("Analise completa com sucesso")