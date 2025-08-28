exports.handler = async (event, context) => {
  const { authorization } = event.headers;
  
  // Basic auth check - substitua 'cordeirotelecom:senha123' pelo seu usuário:senha em base64
  const validAuth = 'Basic Y29yZGVpcm90ZWxlY29tOnNlbmhhMTIz'; // cordeirotelecom:senha123
  
  if (authorization !== validAuth) {
    return {
      statusCode: 401,
      headers: {
        'WWW-Authenticate': 'Basic realm="Socioeducativo"',
        'Content-Type': 'text/html',
      },
      body: `
        <html>
          <head><title>Acesso Restrito</title></head>
          <body>
            <h1>Área Restrita - Socioeducativo</h1>
            <p>Esta área é restrita. Entre em contato com o administrador.</p>
          </body>
        </html>
      `,
    };
  }
  
  // Se autenticado, permita acesso
  return {
    statusCode: 200,
    body: 'OK',
  };
};
