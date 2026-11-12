from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Team

# Create your views here.from django.http import HttpRequest, HttpResponse

teams = {
    "management": Team(
        name="Management Team",
        description="The management team is responsible for overseeing the overall operations and strategic direction of the organization.",
        members=["Brian Scott", "Christopher Labra", "Tristan Herndon"]
    ),
    "procurement": Team(
        name="Procurement Team",
        description="The procurement team is responsible for sourcing and acquiring goods and services needed by the organization.",
        members=["Brian Scott", "Christopher Labra", "Tristan Herndon"]
    ),
    "community": Team(
        name="Community Team",
        description="The community team is responsible for engaging with the local community and building relationships with stakeholders.",
        members=["Tyler Vinsion", "Tyler Joy", "Germaine Reed", "Corey Nixon"]
    ),
    "documentation": Team(
        name="Documentation Team",
        description="The documentation team is responsible for creating and maintaining accurate and up-to-date documentation for the organization's processes, procedures, and systems.",
        members=["Tyler Vinsion", "Tyler Joy", "Germaine Reed", "Corey Nixon"]
    )
}




def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

def team_detail(request, team_name) -> HttpResponse:
    team = teams.get(team_name)
    if team is None:
        return HttpResponse("Team not found", status=404)
    return render(request, 'team_detail.html', {'team': team})
