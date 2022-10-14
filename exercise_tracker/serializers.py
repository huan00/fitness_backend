from exercise.models import Exercise
from rest_framework import serializers
from .models import Session, Workout, ExerciseSet
from exercise.serializers import ExerciseSerializer


class MyExerciseSetSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = ExerciseSet
        fields = (
            'set',
            'rep',
            'weight',
            'exercise',
        )


class ExerciseSetSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = ExerciseSet
        fields = (
            'exercise',
            'set',
            'rep',
            'weight',
        )

    def create(self, validated_data):
        print(validated_data)
        exercise = validated_data.pop('exercise')
        exerciseSet = ExerciseSet.objects.create(**validated_data)
        print('exerciseSet ' + str())

        # Exercise.objects.create(exerciseSet=exerciseSet, **exercise)

        return exerciseSet


class MyWorkoutSerializer(serializers.ModelSerializer):
    exercise_set = MyExerciseSetSerializer(many=True)

    class Meta:
        model = Workout
        fields = (
            'created_at',
            'exercise_set'
        )


class MySessionSerializer(serializers.ModelSerializer):
    workout = MyWorkoutSerializer(many=True)

    class Meta:
        model = Session
        fields = (
            'created_at',
            'workout_day',
            'focus_area',
            'workout'
        )


class WorkoutSerializer(serializers.ModelSerializer):
    exercise_set = ExerciseSetSerializer(many=True)

    class Meta:
        model = Workout
        fields = (
            'exercise_set',
        )

    def create(self, validated_data):
        print('Hello')
        exercises_set_data = validated_data.pop('exercise_set')
        workout = Workout.objects.create(**validated_data)
        print(type(exercises_set_data))

        for exercise_set in exercises_set_data:
            serializer = ExerciseSetSerializer(data=exercise_set)
            print('workout ' + str(serializer.is_valid()))
            if serializer.is_valid():
                serializer.save()
        return workout


class SessionSerializer(serializers.ModelSerializer):
    workout = WorkoutSerializer(many=True)

    class Meta:
        model = Session
        fields = (
            'workout_day',
            'focus_area',
            'workout',
        )

    def create(self, validated_data):
        workouts_data = validated_data.pop('workout')
        # create a session for this entry
        session = Session.objects.create(**validated_data)

        # loop through workout data to create sets
        for workout_data in workouts_data:
            exercises_set = workout_data.pop('exercise_set')
            # create workout associated with session
            workout = Workout.objects.create(session=session, **workout_data)

            # loop through exercises set to create exercise
            for exercise_set in exercises_set:
                exercise = exercise_set.pop('exercise')

                try:
                    # check if exercise exist or not.
                    checkExercise = Exercise.objects.get(name=exercise['name'])

                    # if work out exercise exist append to exercise set, and create exercise set
                    exercise_set['exercise'] = checkExercise
                    ExerciseSet.objects.create(
                        workout=workout, **exercise_set)

                except Exercise.DoesNotExist:
                    # create new exercise if doesn't exist and create exercise set.
                    newExercise = Exercise.objects.create(**exercise)
                    exercise_set['exercise'] = newExercise
                    ExerciseSet.objects.create(
                        workout=workout, **exercise_set)

        return session
