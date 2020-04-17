import { Component, OnInit } from '@angular/core';
import {CompanyService} from '../company.service';
import {ActivatedRoute, Router} from '@angular/router';
import {Vacancy} from '../Vacancy';

@Component({
  selector: 'app-company-vacancies',
  templateUrl: './company-vacancies.component.html',
  styleUrls: ['./company-vacancies.component.css']
})
export class CompanyVacanciesComponent implements OnInit {
  vacancies: Vacancy[];
  constructor(
    private router: Router,
    private companyService: CompanyService,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.getVacancies();
  }
  getVacancies() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.companyService.getVacancyOfCompany(id).subscribe(vacs => this.vacancies = vacs);
  }
}
