from unittest.mock import Mock

from servico_email import ServicoEmail

def test_enviar_email_mock():
    servico = ServicoEmail()
    servico.enviar_email = Mock(return_value="e-mail enviado com sucesso");

    resultado = servico.enviar_email("uepb@edu.br", "acabou a greve")

    assert resultado == "e-mail enviado com sucesso"