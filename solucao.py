"""
Grupo 5 – Desafio de Estrutura de Dados: Hierarquia de Funcionários (Árvores)

Objetivo:
Modelar a hierarquia de uma empresa utilizando a estrutura de dados do tipo árvore N'ária,
em que cada funcionário (nó) pode possuir múltiplos subordinados (filhos).

Requisitos Atendidos:
- Armazenar relações hierárquicas (superior/subordinado)
- Permitir buscar todos os subordinados de um gerente
- Percorrer toda a hierarquia
- Impressão com indentação
- Função para adicionar subordinados
- Percursos: pré-ordem, pós-ordem e em nível

Estrutura Utilizada:
Árvore Genérica (N'ária), onde cada nó possui uma lista de filhos.
Essa é a melhor estrutura para representar relações hierárquicas com múltiplos níveis e múltiplos subordinados.
"""

class Funcionario:
    def __init__(self, nome):
        """Inicializa o funcionário com nome e lista de subordinados."""
        self.nome = nome
        self.subordinados = []

    def adicionar_subordinado(self, subordinado):
        """Adiciona um subordinado direto a este funcionário."""
        self.subordinados.append(subordinado)

    def remover_subordinado(self, nome):
        """Remove um subordinado (direto ou indireto) com base no nome."""
        for i, sub in enumerate(self.subordinados):
            if sub.nome == nome:
                del self.subordinados[i]
                return True
            if sub.remover_subordinado(nome):
                return True
        return False

    def imprimir_hierarquia(self, nivel=0):
        """Imprime a hierarquia com indentação representando níveis."""
        print("  " * nivel + self.nome)
        for sub in self.subordinados:
            sub.imprimir_hierarquia(nivel + 1)

    def buscar_funcionario(self, nome):
        """Busca um funcionário por nome e retorna o nó correspondente."""
        if self.nome == nome:
            return self
        for sub in self.subordinados:
            resultado = sub.buscar_funcionario(nome)
            if resultado:
                return resultado
        return None

    def buscar_subordinados(self):
        """Retorna uma lista com todos os subordinados (diretos e indiretos)."""
        resultado = []
        for sub in self.subordinados:
            resultado.append(sub.nome)
            resultado.extend(sub.buscar_subordinados())
        return resultado

    def contar_subordinados(self):
        """Conta todos os subordinados (diretos e indiretos)."""
        total = len(self.subordinados)
        for sub in self.subordinados:
            total += sub.contar_subordinados()
        return total

    def nivel_hierarquico(self, nome, nivel=0):
        """Retorna o nível hierárquico do funcionário buscado."""
        if self.nome == nome:
            return nivel
        for sub in self.subordinados:
            resultado = sub.nivel_hierarquico(nome, nivel + 1)
            if resultado != -1:
                return resultado
        return -1

    def existe(self, nome):
        """Verifica se um funcionário existe na hierarquia."""
        return self.buscar_funcionario(nome) is not None

    def percurso_pre_ordem(self):
        """Percurso pré-ordem: visita o nó antes dos filhos."""
        resultado = [self.nome]
        for sub in self.subordinados:
            resultado.extend(sub.percurso_pre_ordem())
        return resultado

    def percurso_pos_ordem(self):
        """Percurso pós-ordem: visita os filhos antes do nó."""
        resultado = []
        for sub in self.subordinados:
            resultado.extend(sub.percurso_pos_ordem())
        resultado.append(self.nome)
        return resultado

    def percurso_em_nivel(self):
        """Percurso em nível (BFS): visita por nível hierárquico."""
        resultado = []
        fila = [self]
        while fila:
            atual = fila.pop(0)
            resultado.append(atual.nome)
            fila.extend(atual.subordinados)
        return resultado


if __name__ == "__main__":
    # Exemplo de uso: Construindo uma hierarquia fictícia de empresa
    ceo = Funcionario("CEO")

    diretor_tec = Funcionario("Diretor de Tecnologia")
    diretor_fin = Funcionario("Diretor Financeiro")
    diretor_mkt = Funcionario("Diretor de Marketing")

    gerente_ti = Funcionario("Gerente de TI")
    gerente_dev = Funcionario("Gerente de Desenvolvimento")
    gerente_rh = Funcionario("Gerente de RH")

    analista_ti = Funcionario("Analista de TI")
    DBA_ti = Funcionario("Administrador de banco de dados")
    dev_front = Funcionario("Dev Frontend")
    dev_back = Funcionario("Dev Backend")
    estagiario = Funcionario("Estagiário Dev")

    analista_fin = Funcionario("Analista Financeiro")
    assistente_mkt = Funcionario("Assistente de Marketing")

    # Montando a árvore hierárquica
    ceo.adicionar_subordinado(diretor_tec)
    ceo.adicionar_subordinado(diretor_fin)
    ceo.adicionar_subordinado(diretor_mkt)

    diretor_tec.adicionar_subordinado(gerente_ti)
    diretor_tec.adicionar_subordinado(gerente_dev)

    gerente_ti.adicionar_subordinado(analista_ti)
    gerente_ti.adicionar_subordinado(DBA_ti)
    gerente_dev.adicionar_subordinado(dev_front)
    gerente_dev.adicionar_subordinado(dev_back)
    gerente_dev.adicionar_subordinado(estagiario)

    diretor_fin.adicionar_subordinado(gerente_rh)
    gerente_rh.adicionar_subordinado(analista_fin)

    diretor_mkt.adicionar_subordinado(assistente_mkt)

    # Exibindo os testes e resultados
    print("Hierarquia da empresa:")
    ceo.imprimir_hierarquia()

    print("\nSubordinados de 'Gerente de Desenvolvimento':")
    print(gerente_dev.buscar_subordinados())

    print("\nTotal de subordinados do CEO:", ceo.contar_subordinados())

    print("\nNível de 'Estagiário Dev':", ceo.nivel_hierarquico("Estagiário Dev"))

    print("\nExiste 'Analista de TI'? ", ceo.existe("Analista de TI"))

    print("\nPercurso Pré-Ordem:")
    print(ceo.percurso_pre_ordem())

    print("\nPercurso Pós-Ordem:")
    print(ceo.percurso_pos_ordem())

    print("\nPercurso em Nível (BFS):")
    print(ceo.percurso_em_nivel())

    print("\nRemovendo 'Dev Backend'")
    ceo.remover_subordinado("Dev Backend")

    print("\nNova Hierarquia:")
    ceo.imprimir_hierarquia()
