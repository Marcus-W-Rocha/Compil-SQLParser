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

    def parse_column_list(self):
        while self.token_atual == ",":
            self.match(",")
            self.nextToken()

    def expect_data_type(self):
        self.nextToken()
        token = self.token_atual
        if token not in ('<tipo>', 'int', 'varchar', 'float', 'date', 'datetime', 'char', 'text', 'boolean'):
            raise SyntaxError("Tipo de dado inválido: "+ token)
        else:
            self.nextToken()
        while self.token_atual == ',':
            self.match(",")
            self.nextToken()
            token = self.token_atual
            if token not in ('<tipo>', 'int', 'varchar', 'float', 'date', 'datetime', 'char', 'text', 'boolean'):
                raise SyntaxError("Tipo de dado inválido: "+ token)
            else:
                self.nextToken()

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

# WHERE
    def where(self):
        self.match("WHERE")
        self.nextToken()
        self.match("=")
        self.nextToken()
        
# USE
    def use_statement(self):
        self.match("USE")
        self.nextToken()
        self.match(";")

# CREATE
    def create_statement(self):
        self.match("CREATE")
        if self.token_atual == "DATABASE":
            self.match("DATABASE")
            self.nextToken()

        if self.token_atual == "TABLE":
            self.match("TABLE")
            self.nextToken()
            self.match("(")
            self.expect_data_type()

            self.match(")")
        self.match(";")

# INSERT
    def insert_statement(self):
        self.match("INSERT")
        self.match("INTO")
        self.nextToken()
        self.match("(")
        self.nextToken()
        self.parse_column_list()
        self.match(")")

        self.match("VALUES")
        self.match("(")
        self.nextToken()
        self.parse_column_list()

        self.match(")")
        self.match(";")

# SELECT
    def select_statement(self):
        self.match("SELECT")
        if self.token_atual == "*":
            self.match("*")
            self.match("FROM")
            self.nextToken()
            if self.token_atual == "ORDER":
                self.match("ORDER")
                self.match("BY")
                self.nextToken()
            elif self.token_atual == "WHERE":
                self.where()

        elif self.tokens[self.index_atual+1] == ",":
           self.nextToken()
           self.parse_column_list()
           self.match("FROM")
           self.nextToken()
        self.match(";") 

# UPDATE
    def update_statement(self):
        self.match("UPDATE")
        self.nextToken()
        self.match("SET")
        self.nextToken()
        self.match("=")
        self.nextToken()

        if self.token_atual == "WHERE":
            self.where()
        self.match(";")

# DELETE
    def delete_statement(self):
        self.match("DELETE")
        self.match("FROM")
        self.nextToken()

        if self.token_atual == "WHERE":
            self.where()

        self.match(";")
   
# TRUNCATE
    def truncate_statement(self):
        self.match("TRUNCATE")
        self.match("TABLE")
        self.nextToken()
        self.match(";")

# Exemplo de uso
# query = input("Digite o comando SQL: ")
query = "UPDATE Prova SET Resultado = 'Mesopotâmia' WHERE Questão = 10;"
parser = SQLParser(query)
parser.parse()
print("Analise completa com sucesso\n" + parser.query)
