export interface ApiClientOptions {
  baseUrl: string;
}

export interface ApiClient {
  baseUrl: string;
  request<T>(path: string, init?: RequestInit): Promise<T>;
}

export function createApiClient(options: ApiClientOptions): ApiClient {
  return {
    baseUrl: options.baseUrl,
    async request<T>(path: string, init?: RequestInit): Promise<T> {
      const res = await fetch(`${options.baseUrl}${path}`, init);
      if (!res.ok) {
        throw new Error(`API ${res.status}: ${res.statusText}`);
      }
      return res.json() as Promise<T>;
    },
  };
}
