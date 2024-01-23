import concurrent.futures
import requests
import time
import matplotlib.pyplot as plt
import numpy as np

API_URL = "http://127.0.0.1:5000/upload"

def upload_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            start_time = time.time()
            response = requests.post(API_URL, files=files, timeout=10)  #Timeout adicionado
            end_time = time.time()
            response_time = end_time - start_time
            return response.status_code, response.json(), response_time
    except requests.exceptions.RequestException as e:  #Melhor tratamento de erros
        return 500, {'error': str(e)}, None

def stress_test(num_requests, file_path):

    response_times = []
    successful_requests = 0
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(upload_file, file_path) for _ in range(num_requests)]

        for future in concurrent.futures.as_completed(futures):
            status_code, response_data, response_time = future.result()

            if response_time is not None:
                response_times.append(response_time)
                print(f"Status Code: {status_code}, Response Time: {response_time:.4f} seconds")

            if status_code == 200:
                successful_requests += 1
            else:
                print(f"Failed Request: {response_data}")

            time.sleep(0.1)

    elapsed_time = time.time() - start_time
    requests_per_minute = successful_requests / (elapsed_time / 60)

    #Estatísticas dos tempos de resposta
    avg_response_time = np.mean(response_times)
    median_response_time = np.median(response_times)
    std_dev_response_time = np.std(response_times)
    print(f"Media tempo de resposta: {avg_response_time:.4f} seconds")
    print(f"Mediana tempo de resposta: {median_response_time:.4f} seconds")
    print(f"Desvio padrão dos tempos de resposta: {std_dev_response_time:.4f}")

    #Resultado estresse
    print(f"Total de requisições bem-sucedidas: {successful_requests}")
    print(f"Taxa de requisições bem-sucedidas por minuto: {requests_per_minute:.2f}")

    #Gráficos
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(['Bem-sucedidas', 'Mal-sucedidas'], [successful_requests, num_requests - successful_requests])
    plt.title('Resultado dos testes')
    plt.xlabel('Resultado')
    plt.ylabel('Número de requisições')

    plt.subplot(1, 2, 2)
    plt.hist(response_times, bins=20, color='blue', edgecolor='black')
    plt.title('Distribuição do tempo de resposta')
    plt.xlabel('Tempo de resposta (segundos)')
    plt.ylabel('Frequencia')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    num_requests = 1000  #Esse valor pode ser ajustado
    file_path = '../app/server/NFe_assinada.xml'  #Caminho do arquivo a ser enviado
    stress_test(num_requests, file_path)
