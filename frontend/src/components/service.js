import http from "./http-common";

export default new class Service {
    create(data) {
        return http.post("/tutorials", data);
      }
}