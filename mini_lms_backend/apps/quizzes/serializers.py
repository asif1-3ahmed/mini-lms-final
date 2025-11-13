from rest_framework import serializers
from .models import Quiz, Question, QuizResult

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id","quiz","text","options","correct_index")

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ("id","title","course","questions")

class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResult
        fields = ("id","quiz","student","score","taken_at")
