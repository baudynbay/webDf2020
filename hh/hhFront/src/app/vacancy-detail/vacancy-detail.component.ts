import { Component, OnInit } from '@angular/core';
import {Vacancy} from '../Vacancy';
import {ActivatedRoute, Router} from '@angular/router';
import {CompanyService} from '../company.service';

@Component({
  selector: 'app-vacancy-detail',
  templateUrl: './vacancy-detail.component.html',
  styleUrls: ['./vacancy-detail.component.css']
})
export class VacancyDetailComponent implements OnInit {
  vacancy: Vacancy;
  constructor(
    private router: Router,
    private companyService: CompanyService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    this.getVacancy();
  }
  getVacancy() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.companyService.getVacancy(id).subscribe(vac => this.vacancy = vac);
  }
}
