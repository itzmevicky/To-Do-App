from rest_framework import generics, mixins
from .serializer import *
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class RegisterUser(generics.GenericAPIView):
    
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"User": "Account Created"})


class Todo(generics.CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = TodoTaskSerializer
    queryset = serializer_class.Meta.model.objects.all()


    def get(self, request):
        instance = self.serializer_class.Meta.model.objects.filter(
            createdBy=request.user.id)
        if instance:
            serializer = TodoTaskSerializer(instance, many=True).data
            return Response(serializer)
        return Response("You Haven't Created A Todo List.... :) YET")

    def perform_create(self, serializer):
        createdBy = self.request.user
        Tags = serializer.validated_data.get('Tags') or None
        serializer.save(createdBy=createdBy,Tags=Tags)


class UpdateTask(generics.GenericAPIView, mixins.RetrieveModelMixin):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = TodoTaskSerializer.Meta.model.objects.all()    
    serializer_class = TodoTaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def patch(self, request, *args, **kwargs):
        task_Instance = generics.get_object_or_404(
            TodoTask, pk=kwargs.get('pk'))
        if task_Instance:
            serializer = TodoTaskSerializer(
                instance=task_Instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class DeleteTask(generics.GenericAPIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = TodoTaskSerializer.Meta.model.objects.all()
    serializer_class = TodoTaskSerializer



    def get(self, request, pk):
        instance = generics.get_object_or_404(TodoTask, pk=pk)
        print(instance)
        if instance:
            instance.delete()
            return Response(f'id:{pk} has been deleted')
