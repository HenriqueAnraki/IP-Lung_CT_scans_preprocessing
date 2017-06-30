function [ Cpredicted ] = classify_( )

m = csvread('features.csv');
[lin, col] = size(m);
F=m(:, 2:col-1);
C=m(:, col);
% 10 fold cross validation.
folds = 10;

trainingFunc = @(X, Y) ClassificationKNN.fit(X, Y, ...
                                             'NumNeighbors', 3, ...
                                             'Distance', 'cityblock');

CVO = cvpartition(C, 'k', folds);
Acc = zeros(CVO.NumTestSets,1);
for i = 1:CVO.NumTestSets
    trIdx = CVO.training(i);
    teIdx = CVO.test(i);
    
    cl = trainingFunc(F(trIdx,:), C(trIdx,:));
    actualClass = C(teIdx);
    predClass = predict(cl, F(teIdx,:));
    
    right = 0;
    wrong = 0;
    for idx = 1:numel(actualClass)
        if actualClass(idx) == predClass(idx)
            right = right + 1;
        else
            wrong = wrong + 1;
        end
    end
    
    % Accurracy of this fold validation
    Acc(i) = (right)/sum(right + wrong);
end

fprintf('%d-Fold Cross Validation on ROIs\n', folds);
fprintf('\tAcc = %.3f +- %.3f\n', mean(Acc), std(Acc));

% Outputs the vector of predicted classes
cl = trainingFunc(F, C);
Cpredicted = predict(cl, F);

end
