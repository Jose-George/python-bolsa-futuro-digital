# 📝 **Lista de Exercícios – Clean Code + Boas Práticas no Django REST**

## ✅ **Exercício 1 — Refatoração de Código Sujo (Nível: Raciocínio + Análise)**

Você recebeu o seguinte código de uma API que cria produtos. Ele funciona, mas está **cheio de más práticas**, violando princípios de Clean Code, SOLID e separação de responsabilidades:

```python
# views.py
class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def create(self, request):
        data = request.data

        if "nome" not in data or data["nome"] == "":
            return Response({"erro": "Nome obrigatório"}, status=400)

        if Produto.objects.filter(nome=data["nome"]).exists():
            return Response({"erro": "Produto já existe"}, status=400)

        produto = Produto.objects.create(
            nome=data["nome"],
            preco=float(data.get("preco", 0)),
            estoque=int(data.get("estoque", 0))
        )

        print("Produto criado:", produto.id)

        return Response({"mensagem": "ok"}, status=200)
```

### 🎯 **Seu desafio é:**

1. Identificar **no mínimo 5 problemas** de Clean Code e boas práticas nesse código (explique cada um).
2. Reescrever a solução aplicando:

   * Validações no **serializer**
   * Regra de negócio em um **service**
   * Nada de prints; use logging se necessário
   * `status code` apropriado
   * Views magras
   * Reposta padronizada
3. Criar a estrutura final:

   * `services.py`
   * `serializers.py`
   * `views.py` (refatorado)

👉 O objetivo é você **analisar**, **decidir**, **refatorar** e provar que entendeu a arquitetura limpa.

---

## ✅ **Exercício 2 — Criar uma API seguindo Clean Code (Nível: Raciocínio + Modelagem)**

Crie um novo app chamado **tarefas**, com uma API de **to-do list**, respeitando todos os princípios de Clean Code.

A entidade **Tarefa** deve ter:

* `titulo` (obrigatório)
* `descricao`
* `prioridade` (opções: baixa, media, alta)
* `concluida` (booleano, padrão False)
* `created_at` (auto)
* `updated_at` (auto)

### 🎯 **Requisitos obrigatórios:**

1. **Modelagem limpa**

   * Nomes claros
   * Campos corretos
   * Sem gorduras

2. **Serializer com validações**

   * Valide se o título está vazio
   * Valide se a prioridade é uma das opções válidas

3. **Camada de serviço**
   Crie o arquivo `services.py` com funções:

   * `create_tarefa_service(data)`
   * `update_tarefa_service(instance, data)`

4. **ViewSet magro**

   * A view deve apenas chamar os services
   * Use respostas padronizadas
   * Use os status codes corretos

5. **URLs limpas**

   * `/tarefas/`
   * `/tarefas/<id>/`

6. **Desafio extra (opcional, mas recomendado):**
   Criar um endpoint customizado:

   ```
   PATCH /tarefas/<id>/concluir/
   ```

   Essa rota deve:

   * Marcar como concluída
   * Retornar mensagem clara
   * Seguir clean code

### 🧠 **O que esse exercício testa**

* Raciocínio de modelagem
* Organização por camadas
* Clareza e limpeza de código
* Raciocínio de API REST
* Uso adequado de serializer + service + view
