# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LABEL_ELDERLY_SUBJECT_METADATA = Metadata(
    id="49fd247159ed8fb4cfcd93e1479cc302731742ef.boutiques",
    name="label_elderly_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


LabelElderlySubjectParameters = typing.TypedDict('LabelElderlySubjectParameters', {
    "__STYXTYPE__": typing.Literal["label_elderly_subject"],
    "norm_volume": InputPathType,
    "transform_lta": InputPathType,
    "classifier_array": typing.NotRequired[InputPathType | None],
    "aseg_volume": InputPathType,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "label_elderly_subject": label_elderly_subject_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "label_elderly_subject": label_elderly_subject_outputs,
    }.get(t)


class LabelElderlySubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_elderly_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    labeled_volume: OutputPathType
    """Labeled output volume"""


def label_elderly_subject_params(
    norm_volume: InputPathType,
    transform_lta: InputPathType,
    aseg_volume: InputPathType,
    classifier_array: InputPathType | None = None,
) -> LabelElderlySubjectParameters:
    """
    Build parameters.
    
    Args:
        norm_volume: Normalized input volume (e.g. norm.mgz).
        transform_lta: Transformation file (e.g. talairach.lta).
        aseg_volume: Asegmentation volume file (e.g. aseg.mgz).
        classifier_array: Classifier array file (e.g. mixed.gca).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label_elderly_subject",
        "norm_volume": norm_volume,
        "transform_lta": transform_lta,
        "aseg_volume": aseg_volume,
    }
    if classifier_array is not None:
        params["classifier_array"] = classifier_array
    return params


def label_elderly_subject_cargs(
    params: LabelElderlySubjectParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("label_elderly_subject")
    cargs.append(execution.input_file(params.get("norm_volume")))
    cargs.append(execution.input_file(params.get("transform_lta")))
    if params.get("classifier_array") is not None:
        cargs.append(execution.input_file(params.get("classifier_array")))
    cargs.append(execution.input_file(params.get("aseg_volume")))
    return cargs


def label_elderly_subject_outputs(
    params: LabelElderlySubjectParameters,
    execution: Execution,
) -> LabelElderlySubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LabelElderlySubjectOutputs(
        root=execution.output_file("."),
        labeled_volume=execution.output_file(pathlib.Path(params.get("aseg_volume")).name + "_labeled.mgz"),
    )
    return ret


def label_elderly_subject_execute(
    params: LabelElderlySubjectParameters,
    execution: Execution,
) -> LabelElderlySubjectOutputs:
    """
    Tool for labeling brain structures in MRI images of elderly subjects using
    Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LabelElderlySubjectOutputs`).
    """
    params = execution.params(params)
    cargs = label_elderly_subject_cargs(params, execution)
    ret = label_elderly_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def label_elderly_subject(
    norm_volume: InputPathType,
    transform_lta: InputPathType,
    aseg_volume: InputPathType,
    classifier_array: InputPathType | None = None,
    runner: Runner | None = None,
) -> LabelElderlySubjectOutputs:
    """
    Tool for labeling brain structures in MRI images of elderly subjects using
    Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        norm_volume: Normalized input volume (e.g. norm.mgz).
        transform_lta: Transformation file (e.g. talairach.lta).
        aseg_volume: Asegmentation volume file (e.g. aseg.mgz).
        classifier_array: Classifier array file (e.g. mixed.gca).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelElderlySubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_ELDERLY_SUBJECT_METADATA)
    params = label_elderly_subject_params(
        norm_volume=norm_volume,
        transform_lta=transform_lta,
        classifier_array=classifier_array,
        aseg_volume=aseg_volume,
    )
    return label_elderly_subject_execute(params, execution)


__all__ = [
    "LABEL_ELDERLY_SUBJECT_METADATA",
    "LabelElderlySubjectOutputs",
    "LabelElderlySubjectParameters",
    "label_elderly_subject",
    "label_elderly_subject_params",
]
