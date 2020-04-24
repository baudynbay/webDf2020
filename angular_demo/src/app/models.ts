export class Company {
  id: number;
  name: string;
  description: string;
  city: string;
  address: string;
}

export class Vacancy {
  id: number;
  name: string;
  description: string;
  salary: string;
  company: Company;
}

export class LoginResponse {
  token: string;
}
