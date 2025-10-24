# Exercícios — pratique no MyCompiler

Execute cada consulta e observe os resultados. Tente primeiro escrever a query sozinho; se travar, reveja os exemplos da aula.

1. **Listar todos os pedidos com o nome do cliente**
   Mostre: `id_pedido`, `nome` e `valor`. Use `INNER JOIN`.

2. **Listar todos os clientes e seus pedidos (se houver)**
   Mostre: `id_cliente`, `nome`, `id_pedido`, `valor`. Use `LEFT JOIN` para que clientes sem pedidos também apareçam.

3. **Quantos pedidos cada cliente realizou?**
   Resultado: `nome`, `qtd_pedidos`. Ordene pelo número de pedidos decrescente.

4. **Qual o total gasto por cliente?**
   Resultado: `nome`, `total_gasto` (soma dos valores). Mostre também clientes com `total_gasto = 0` (se possível).

5. **Qual a média do valor dos pedidos por cliente?**
   Resultado: `nome`, `media_pedido`. Exiba apenas clientes que tenham pelo menos 1 pedido.

6. **Total de pedidos e soma dos valores por cidade**
   Resultado: `cidade`, `qtd_pedidos`, `total_vendas`. Ordene pelas `total_vendas` em ordem decrescente.

7. **Encontre o pedido de maior valor e exiba o nome do cliente**
   Mostre `id_pedido`, `valor`, `nome` do cliente que tem o pedido com maior `valor`.

8. **Liste os 3 clientes que mais gastaram (top 3)**
   Resultado: `nome`, `total_gasto`. Use `ORDER BY` e `LIMIT`.

9. **Quantos pedidos foram feitos entre 2025-03-01 e 2025-07-31?**
   Mostre a quantidade e também a soma dos valores nesse intervalo de datas.

10. **Mostrar clientes cujo total gasto seja maior que 200**
    Use `GROUP BY` + `HAVING` para filtrar clientes que gastaram mais de 200. Resultado: `nome`, `total_gasto`.

