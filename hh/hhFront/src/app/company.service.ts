import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Company} from './Company';
import {Vacancy} from './Vacancy';
import {tap} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  logged = false;
  BASE_URL = 'http://localhost:8000';
  constructor(private http: HttpClient) { }

  getCompanies(): Observable<Company[]> {
      return this.http.get<Company[]>(`${this.BASE_URL}/api/companies`)
  }
  getVacancyOfCompany(companyId): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${companyId}/vacancies`);
  }
  getCompany(companyId): Observable<Company> {
    return this.http.get<Company>(`${this.BASE_URL}/api/companies/${companyId}`);
  }
  getVacancy(id: number): Observable<Vacancy> {
    return this.http.get<Vacancy>(`${this.BASE_URL}/api/vacancies/${id}`);
  }
  getVacancies(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/vacancies`);
  }
}
