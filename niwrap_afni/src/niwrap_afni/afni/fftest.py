# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FFTEST_METADATA = Metadata(
    id="242a4a37e8f3488a79d04ee8e61c7d3309af7f5b.boutiques",
    name="fftest",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


FftestParameters = typing.TypedDict('FftestParameters', {
    "__STYXTYPE__": typing.Literal["fftest"],
    "length": float,
    "num_tests": float,
    "vector_size": float,
    "quiet_mode": bool,
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
        "fftest": fftest_cargs,
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


class FftestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fftest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fftest_params(
    length: float,
    num_tests: float,
    vector_size: float,
    quiet_mode: bool = False,
) -> FftestParameters:
    """
    Build parameters.
    
    Args:
        length: Length of the test.
        num_tests: Number of tests to run.
        vector_size: Vector size for the test.
        quiet_mode: Quiet mode.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fftest",
        "length": length,
        "num_tests": num_tests,
        "vector_size": vector_size,
        "quiet_mode": quiet_mode,
    }
    return params


def fftest_cargs(
    params: FftestParameters,
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
    cargs.append("fftest")
    cargs.append(str(params.get("length")))
    cargs.append(str(params.get("num_tests")))
    cargs.append(str(params.get("vector_size")))
    if params.get("quiet_mode"):
        cargs.append("-q")
    return cargs


def fftest_outputs(
    params: FftestParameters,
    execution: Execution,
) -> FftestOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FftestOutputs(
        root=execution.output_file("."),
    )
    return ret


def fftest_execute(
    params: FftestParameters,
    execution: Execution,
) -> FftestOutputs:
    """
    A command line tool for testing purposes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FftestOutputs`).
    """
    params = execution.params(params)
    cargs = fftest_cargs(params, execution)
    ret = fftest_outputs(params, execution)
    execution.run(cargs)
    return ret


def fftest(
    length: float,
    num_tests: float,
    vector_size: float,
    quiet_mode: bool = False,
    runner: Runner | None = None,
) -> FftestOutputs:
    """
    A command line tool for testing purposes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        length: Length of the test.
        num_tests: Number of tests to run.
        vector_size: Vector size for the test.
        quiet_mode: Quiet mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FftestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FFTEST_METADATA)
    params = fftest_params(
        length=length,
        num_tests=num_tests,
        vector_size=vector_size,
        quiet_mode=quiet_mode,
    )
    return fftest_execute(params, execution)


__all__ = [
    "FFTEST_METADATA",
    "FftestOutputs",
    "FftestParameters",
    "fftest",
    "fftest_params",
]
