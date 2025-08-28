exports.handler = async (event, context) => {
  const { authorization } = event.headers;
  
  // Credenciais válidas - altere conforme necessário
  const validCredentials = {
    username: 'cordeirotelecom',
    password: 'Socio2025!@#'  // Senha forte sugerida
  };
  
  // Codificar credenciais em base64
  const validAuth = 'Basic ' + Buffer.from(
    `${validCredentials.username}:${validCredentials.password}`
  ).toString('base64');
  
  // Verificar autenticação
  if (!authorization || authorization !== validAuth) {
    return {
      statusCode: 401,
      headers: {
        'WWW-Authenticate': 'Basic realm="Área Socioeducativo - Acesso Restrito"',
        'Content-Type': 'text/html; charset=utf-8',
      },
      body: `
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Acesso Restrito - Socioeducativo</title>
          <style>
            body { 
              font-family: Arial, sans-serif; 
              background: #f5f5f5; 
              padding: 2rem; 
              text-align: center; 
            }
            .container { 
              max-width: 500px; 
              margin: 0 auto; 
              background: white; 
              padding: 2rem; 
              border-radius: 8px; 
              box-shadow: 0 2px 10px rgba(0,0,0,0.1); 
            }
            h1 { color: #d63031; }
            p { color: #666; line-height: 1.6; }
          </style>
        </head>
        <body>
          <div class="container">
            <h1>🔒 Área Restrita</h1>
            <h2>Socioeducativo - Informática Básica</h2>
            <p>Esta área contém material específico para atividades de ressocialização.</p>
            <p><strong>Acesso permitido apenas para educadores autorizados.</strong></p>
            <p>Entre em contato com o administrador do sistema para obter credenciais de acesso.</p>
            <hr>
            <p><small>Sistema desenvolvido por cordeirotelecom</small></p>
          </div>
        </body>
        </html>
      `,
    };
  }
  
  // Se autenticado corretamente, redirecionar para o conteúdo solicitado
  const requestedPath = event.path.replace('/socioeducativo/', '');
  const targetUrl = `/socioeducativo/${requestedPath}`;
  
  return {
    statusCode: 302,
    headers: {
      'Location': targetUrl,
      'Cache-Control': 'no-cache',
    },
    body: '',
  };
};
