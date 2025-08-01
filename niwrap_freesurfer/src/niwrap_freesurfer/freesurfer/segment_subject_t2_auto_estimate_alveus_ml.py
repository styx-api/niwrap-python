# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SEGMENT_SUBJECT_T2_AUTO_ESTIMATE_ALVEUS_ML_METADATA = Metadata(
    id="e6b692a7de46610579fa5e10ad01fb96c5b2f745.boutiques",
    name="segmentSubjectT2_autoEstimateAlveusML",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


SegmentSubjectT2AutoEstimateAlveusMlParameters = typing.TypedDict('SegmentSubjectT2AutoEstimateAlveusMlParameters', {
    "__STYXTYPE__": typing.Literal["segmentSubjectT2_autoEstimateAlveusML"],
    "missing_library": str,
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
        "segmentSubjectT2_autoEstimateAlveusML": segment_subject_t2_auto_estimate_alveus_ml_cargs,
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
    }.get(t)


class SegmentSubjectT2AutoEstimateAlveusMlOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subject_t2_auto_estimate_alveus_ml(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def segment_subject_t2_auto_estimate_alveus_ml_params(
    missing_library: str = "libmwlaunchermain.so: cannot open shared object file",
) -> SegmentSubjectT2AutoEstimateAlveusMlParameters:
    """
    Build parameters.
    
    Args:
        missing_library: The tool could not be executed due to a missing shared\
            library: libmwlaunchermain.so.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "segmentSubjectT2_autoEstimateAlveusML",
        "missing_library": missing_library,
    }
    return params


def segment_subject_t2_auto_estimate_alveus_ml_cargs(
    params: SegmentSubjectT2AutoEstimateAlveusMlParameters,
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
    cargs.append("segmentSubjectT2_autoEstimateAlveusML")
    cargs.append(params.get("missing_library"))
    return cargs


def segment_subject_t2_auto_estimate_alveus_ml_outputs(
    params: SegmentSubjectT2AutoEstimateAlveusMlParameters,
    execution: Execution,
) -> SegmentSubjectT2AutoEstimateAlveusMlOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SegmentSubjectT2AutoEstimateAlveusMlOutputs(
        root=execution.output_file("."),
    )
    return ret


def segment_subject_t2_auto_estimate_alveus_ml_execute(
    params: SegmentSubjectT2AutoEstimateAlveusMlParameters,
    execution: Execution,
) -> SegmentSubjectT2AutoEstimateAlveusMlOutputs:
    """
    A Freesurfer tool to segment T2 subjects with automatic alveus ML estimation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectT2AutoEstimateAlveusMlOutputs`).
    """
    params = execution.params(params)
    cargs = segment_subject_t2_auto_estimate_alveus_ml_cargs(params, execution)
    ret = segment_subject_t2_auto_estimate_alveus_ml_outputs(params, execution)
    execution.run(cargs)
    return ret


def segment_subject_t2_auto_estimate_alveus_ml(
    missing_library: str = "libmwlaunchermain.so: cannot open shared object file",
    runner: Runner | None = None,
) -> SegmentSubjectT2AutoEstimateAlveusMlOutputs:
    """
    A Freesurfer tool to segment T2 subjects with automatic alveus ML estimation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        missing_library: The tool could not be executed due to a missing shared\
            library: libmwlaunchermain.so.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectT2AutoEstimateAlveusMlOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_SUBJECT_T2_AUTO_ESTIMATE_ALVEUS_ML_METADATA)
    params = segment_subject_t2_auto_estimate_alveus_ml_params(
        missing_library=missing_library,
    )
    return segment_subject_t2_auto_estimate_alveus_ml_execute(params, execution)


__all__ = [
    "SEGMENT_SUBJECT_T2_AUTO_ESTIMATE_ALVEUS_ML_METADATA",
    "SegmentSubjectT2AutoEstimateAlveusMlOutputs",
    "SegmentSubjectT2AutoEstimateAlveusMlParameters",
    "segment_subject_t2_auto_estimate_alveus_ml",
    "segment_subject_t2_auto_estimate_alveus_ml_params",
]
