#include <WiFi.h>
#include <WebServer.h>

// Coloque o nome e senha do Wi-Fi do laboratório
const char* ssid = "WIFI-EDUC";
const char* password = "ac5ce0ss7@educ";

// Vamos usar o pino 2 (LED embutido na maioria dos ESP32)
const int PINO_MAQUINA = 19; 



// Cria o servidor web na porta padrão (80)
WebServer server(80);

void setup() {
  Serial.begin(115200);
  pinMode(PINO_MAQUINA, OUTPUT);
  digitalWrite(PINO_MAQUINA, LOW); // Começa desligado
  pintMode(2,OUTPUT)

  // 1. Conectando no Wi-Fi
  Serial.print("Conectando ao Wi-Fi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado!");
  Serial.print("Endereço IP do ESP32: ");
  Serial.println(WiFi.localIP()); // Esse é o IP que vai no código Python da IA!
  digitalWrite(2,HIGH)

  // 2. Criando as rotas que a IA vai acessar
  
  // Rota para LIGAR
  server.on("/ligar", []() {
    digitalWrite(PINO_MAQUINA, HIGH); // Liga o pino (ou relé)
    server.send(200, "text/plain", "Maquina LIGADA com sucesso!");
    Serial.println("Comando recebido: LIGAR");
  });

  // Rota para DESLIGAR
  server.on("/desligar", []() {
    digitalWrite(PINO_MAQUINA, LOW); // Desliga o pino (ou relé)
    server.send(200, "text/plain", "Maquina DESLIGADA com sucesso!");
    Serial.println("Comando recebido: DESLIGAR");
  });

  // 3. Inicia o servidor
  server.begin();
  Serial.println("Servidor Web rodando e aguardando a IA...");
}

void loop() {
  // Mantém o servidor escutando os pedidos da rede
  server.handleClient();
}