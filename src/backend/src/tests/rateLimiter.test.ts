import request from "supertest";
import app from "../app";

describe('Teste da rota raiz', () => {
    it('deve responder com mensagem de boas-vindas', async () => {
      const response = await request(app).get('/');
      expect(response.statusCode).toBe(200);
      expect(response.body).toEqual({ message: 'Hello world' });
    });
  
    it('deve bloquear o usuário após exceder o limite de requisições', async () => {
      // Fazendo requisições repetidas
      for (let i = 0; i < 3; i++) {
        await request(app).get('/');
      }
  
      // A próxima requisição deve ser bloqueada
      const response = await request(app).get('/');
      expect(response.statusCode).toBe(429);
      expect(response.body).toEqual({ message: 'Muitas requisições. Tente novamente mais tarde.' });
    });
  });
  