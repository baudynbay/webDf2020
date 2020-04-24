import { Component, OnInit } from '@angular/core';
import {VacancyService} from '../vacancy.service';
import {ActivatedRoute} from '@angular/router';
import {Vacancy} from '../models';

@Component({
  selector: 'app-vacancy-detail',
  templateUrl: './vacancy-detail.component.html',
  styleUrls: ['./vacancy-detail.component.css']
})
export class VacancyDetailComponent implements OnInit {
  vacancy: Vacancy;
  vacancyId: string;
  constructor(private vacancyService: VacancyService, private route: ActivatedRoute) {
    this.route.paramMap.subscribe(params => {
      this.vacancyId = params.get('vacancyId');
    });
  }

  ngOnInit(): void {
    this.getVacancyById(this.vacancyId);
  }
  getVacancyById(id: string) {
    this.vacancyService.getVacancyById(id)
      .subscribe(vacancy => {
        this.vacancy = vacancy;
      });
  }
}
